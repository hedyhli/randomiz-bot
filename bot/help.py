from discord.ext.commands import HelpCommand, Cog
from discord import Embed


class BotHelpCommand(HelpCommand):
    async def send_bot_help(self, mapping):
        """Sends a help message"""

        commands_obj = next(iter(mapping.values()))
        commands_help = [
            "`" + self.get_command_signature(i) + "`" for i in commands_obj
        ]

        for i in range(len(commands_help)):
            commands_help[i] += " - "
            commands_help[i] += commands_obj[i].short_doc + "\n"

        embed = (
            Embed(
                title="Help for The Randomiz Bot",
                description="A utility bot that provides you commands to get random integers, choices, and more",
                colour=0x41C03F,
            )
            .add_field(
                name=f"\u200b\n** Commands**",
                value="\n".join(commands_help),
                inline=False,
            )
            .add_field(
                name="\u200b\n**Still need help?**",
                value="Join the [bot support server](https://discord.gg/uwyYpt9) for additional help",
                inline=False,
            )
        )

        await self.context.send(embed=embed)
