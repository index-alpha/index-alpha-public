# Open Source Curator

Read the [Index run contract](../../README.md), [definition](../../definition.md),
and [common workflow](../../../workflow.md). Use the
[maintained Index Alpha skill](../../../../skills/index-alpha/SKILL.md).

Choose the requested bounded task:

- [select.md](select.md): inspect at most 15 fixed candidate identities; select at most three.
- [create.md](create.md): create at most three qualified supplied cards.
- [maintain.md](maintain.md): check at most five due cards.

Use platform reads for observable facts and host-supplied exact targets plus
in-memory run context/source cache/evidence for handoffs. Optional `state_dir`
holds only sparse text checkpoints in owner-private
`common/state/<agent-id>/`; missing remote files do not block discovery. Apply/maintain
intent and mode carry through all requested stages under the common workflow;
loading these files grants no platform access. Initial private setup uses
[setup](../../../setup.md). Shared review/formatting follows the Index run contract
with the same run context/evidence, inherited mode, definition, exact cards, and
invocation deadline.
