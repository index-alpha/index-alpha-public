schemas = JSON.parse(File.read(ARGV.fetch(0)))
skill_dir = ARGV.fetch(1)
map = File.read(File.join(skill_dir, "references/mcp-server-map.md"))
block = map[/<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->(.*?)<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->/m, 1]
abort "error: documented tool inventory block missing" unless block
documented = block.scan(/^- ([a-z0-9_]+)$/).flatten
abort "error: duplicate tools in documented inventory" unless documented.uniq == documented
missing = schemas.keys - documented
extra = documented - schemas.keys
abort "error: inventory drift; missing=#{missing.inspect}, extra=#{extra.inspect}" unless missing.empty? && extra.empty?
puts "==> inventory matches #{schemas.size} effective tool schemas"

# Check field shapes (required, unknown, nested object/array, selector oneOf).
# This checks documented field shapes, not full JSON Schema or runtime semantics.
def check_shape(value, schema, path)
  return unless schema.is_a?(Hash)
  if value.is_a?(Hash)
    missing = Array(schema["required"]) - value.keys
    abort "error: #{path} missing fields #{missing.inspect}" unless missing.empty?
    properties = schema.fetch("properties", {})
    if schema["additionalProperties"] == false
      extra = value.keys - properties.keys
      abort "error: #{path} unknown fields #{extra.inspect}" unless extra.empty?
    end
    if schema["oneOf"]
      matches = schema["oneOf"].count { |choice| (Array(choice["required"]) - value.keys).empty? }
      abort "error: #{path} must match exactly one selector" unless matches == 1
    end
    value.each { |key, item| check_shape(item, properties[key], "#{path}.#{key}") }
  elsif value.is_a?(Array)
    value.each_with_index { |item, i| check_shape(item, schema["items"], "#{path}[#{i}]") }
  end
end

examples_dir = ARGV.fetch(2)
abort "error: workflow examples directory missing" unless File.directory?(examples_dir)
examples = 0
files = [skill_dir, examples_dir].flat_map { |root| Dir.glob(File.join(root, "**/*.md")) }
files.sort.each do |file|
  File.read(file).scan(/```json\n(.*?)\n```/m).each do |match|
    example = JSON.parse(match.first)
    next unless example.is_a?(Hash) && example.key?("tool")
    tool = example.fetch("tool")
    abort "error: unknown example tool #{tool}" unless schemas.key?(tool)
    check_shape(example.fetch("arguments"), schemas.fetch(tool).fetch("input"), "#{file}:#{tool}")
    examples += 1
  end
end
abort "error: no tool invocation examples checked" if examples.zero?
puts "==> #{examples} documented example argument shapes checked"
