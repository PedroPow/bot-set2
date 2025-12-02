from unicodedata import name
import discord
from discord.ext import commands
from discord.ui import View, Button, Select, Modal, TextInput
from discord import Embed, TextStyle
import asyncio
import os
import sys
sys.modules['audioop'] = None


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# CONFIGURAÇÃO
TOKEN = os.getenv("TOKEN")
CANALETA_SOLICITAR_SET_ID = 1373877635041464432
CARGO_NOVATO_ID = 1363298591614963772
CATEGORIA_TICKET_ID = 1373846163366875146  # <- Substitua pelo ID correto da categoria dos tickets

COMPANHIAS_CHANNEL = {
    "QCG": 1367377415357333544,
    "CORREGEDORIA": 1367377491538477186, 
    "CAvPM": 1367377579283185744,
    "21 BPM": 1367377653216186378,
    "FORÇA TÁTICA": 1367377719888707615,
    "BAEP": 1367377813748842617,
    "1° BPCHQ ROTA": 1367377873199173682,
    "2° BPCHQ ANCHIETA": 1367377927905214524,
    "3° BPCHQ HUMAITÁ": 1367378044930494514,
    "4° BPCHQ COE": 1367378044930494514,
    "GCM" : 1389766870378348554,
    "PCESP": 1367378110303178834, 
    "GARRA" : 1398862056416870564,
    "DHPP" : 1398862133424422972,
    "DOPE" : 1398862221093900438,
    "DEIC" : 1398862292342407348,
    "GER" : 1398862330883997726,
}

CARGOS_COMPANHIA = {
    "QCG": 1362609132716167279, 
    "CORREGEDORIA": 1368694431946903744, 
    "CAvPM": 1368695624517681324,
    "21 BPM": 1362602084477702224,
    "FORÇA TÁTICA": 1376353262390874263,
    "BAEP": 1368752196052582442,
    "1° BPCHQ ROTA": 1362613766176505916,
    "2° BPCHQ ANCHIETA": 1368752340450017341,
    "3° BPCHQ HUMAITÁ": 1368752346015862855,
    "4° BPCHQ COE": 1368752343679762452,
    "GCM" : 1389767734220554250,
    "PCESP": 1368759311316291664,
    "GARRA": 1368759311316291664,
    "DHPP": 1368759311316291664,
    "DOPE": 1368759311316291664,
    "DEIC": 1368759311316291664,
    "GER": 1368759311316291664,   
}

PATENTES = {
    "[] Soldado de 2º Classe PM": 1362602895391981689,
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    "[✵✵✵] Coronel PM": 1362602399189172244,
}

PATENTES_PCESP = {
    "Acadepol" : 1398846067096944750,
    "Escrivães de Polícia": 1368059603241406484,
    "Investigador de Polícia": 1368060090439045160,
    "Agentes de Polícia": 1368060178263576647,
    "Delegado de Polícia": 1368060294689194024,
    "Perito Criminal": 1368060367280017489,
    "Perito Técnico": 1368061324562792528,
    "Delegado Adjunto": 1368060423370309704,
    "Chefe de Polícia": 1368060484695228477,
    "Delegado Geral": 1368060540483538954,
}

PATENTES_GARRA = {
    "Acadepol" : 1398846067096944750,
    "Agentes 3° classe" : 1398854786375483495,
    "Agentes 2° classe" : 1398854883213443102,
    "Agentes 1° classe" : 1398854903425667195,
    "Agentes Classe Especial" :1398854928503537795,
    "Investigador de Polícia 3° classe" : 1398855953243439134,
    "Investigador de Polícia 2° classe" : 1398856004397170708,
    "Investigador de Polícia 1° classe" : 1398856024525635605,
    "Investigador de Polícia Classe Especial" : 1398856451790864495,
    "Delegado Adjunto" : 1368060423370309704,
    "Delegado Garra" : 1398859977036136490,
    "Diretor Garra / Dope" : 1398860090513293453,
}

PATENTES_DHPP = {
    "Acadepol" : 1398846067096944750,
    "Agentes 3° classe" : 1398854786375483495,
    "Agentes 2° classe" : 1398854883213443102,
    "Agentes 1° classe" : 1398854903425667195,
    "Agentes Classe Especial" :1398854928503537795,
    "Escrivães de Polícia": 1368059603241406484,
    "Delegados Operacionais" : 1398860363725930587,
    "Delegado Adjunto" : 1368060423370309704,
    "Delegado DHPP" : 1398860587378933841,
}

PATENTES_DOPE = {
    "Acadepol" : 1398846067096944750,
    "Agentes 3° classe" : 1398854786375483495,
    "Agentes 2° classe" : 1398854883213443102,
    "Agentes 1° classe" : 1398854903425667195,
    "Agentes Classe Especial" :1398854928503537795,
    "Investigador de Polícia 3° classe" : 1398855953243439134,
    "Investigador de Polícia 2° classe" : 1398856004397170708,
    "Investigador de Polícia 1° classe" : 1398856024525635605,
    "Investigador de Polícia Classe Especial" : 1398856451790864495,
    "Delegado Adjunto" : 1368060423370309704,
    "Delegado Garra" : 1398859977036136490,
    "Diretor Garra / Dope" : 1398860090513293453,
}

PATENTES_DEIC = {
    "Acadepol" : 1398846067096944750,
    "Agentes 3° classe" : 1398854786375483495,
    "Agentes 2° classe" : 1398854883213443102,
    "Agentes 1° classe" : 1398854903425667195,
    "Agentes Classe Especial" : 1398854928503537795,
    "Escrivães de Polícia": 1368059603241406484,
    "Perito Criminal": 1368060367280017489,
    "Delegado Adjunto" : 1368060423370309704,
    "Delegado DEIC" : 1398859713042714704,
}

PATENTES_GER = {
    "Acadepol" : 1398846067096944750,
    "Agentes 3° classe" : 1398854786375483495,
    "Agentes 2° classe" : 1398854883213443102,
    "Agentes 1° classe" : 1398854903425667195,
    "Agentes Classe Especial" : 1398854928503537795,
    "Especialistas em Breach": 1398857381814993087,
    "Investigador Tático Classe Inicial" : 1398857509208457238,
    "Investigador Tático 3° classe" : 1398857555748327424,
    "Investigador Tático 2° classe" : 1398857671305859092,
    "Investigador Tático 1° classe" : 1398857735038177320,
    "Investigador Tático Classe Especial" : 1398857820530806874,
    "Investigador Chefe" : 1398857941674627184,
    "Delegado Operacional GER" : 1398858935330537573,
    "Delegado Supervisor GER" : 1398859110077698058,
}

PATENTES_ESPECIALIZADAS = {

    "GCM": {
    "Terceira Classe": 1389772575932158002,
    "Segunda Classe": 1389772623621394524,
    "Primeira Classe": 1389772644135731402,
    "Classe Especial": 1389772671876862093,
    "Inspetor de Terceira Classe": 1389772697038491689,
    "Inspetor de Segunda Classe": 1389772714255974570,
    "Inspetor de Primeira Classe": 1389772739983835176,
    },

    "BAEP": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    },

    "CORREGEDORIA": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    "[✵✵✵] Coronel PM": 1362602399189172244,
    },

    "FORÇA TÁTICA": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    },

    "1° BPCHQ ROTA": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    },
    "2° BPCHQ ANCHIETA": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    },
    "3° BPCHQ HUMAITÁ": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    },
    "4° BPCHQ COE": {
    "[❯] Soldado de 1º Classe PM": 1362602865285140490,
    "[❯❯] Cabo PM": 1362602838928134345,
    "[❯❯❯] 3º Sargento PM": 1362602768732393503,
    "[❯ ❯❯❯] 2º Sargento PM": 1362602740160790599,
    "[❯❯ ❯❯❯] 1º Sargento PM": 1362602703707963484,
    "[△] Sub-Tenente PM": 1362602675312787526,
    "[✯] Aspirante a Oficial PM": 1362602649307844838,
    "[✧] 2º Tenente PM": 1362602616348999781,
    "[✧✧] 1º Tenente PM": 1362602576419360778,
    "[✧✧✧] Capitão PM": 1362602545897537768,
    "[✵✧✧] Major PM": 1362602512120549499,
    "[✵✵✧] Tenente Coronel PM": 1362602485092581586,
    }

    
}
solicitacoes_abertas = {}

def get_patentes_para(companhia):

    # 1 — Se estiver nas especializadas
    if companhia in PATENTES_ESPECIALIZADAS:
        return PATENTES_ESPECIALIZADAS[companhia]

    # 2 — Tabelas individuais
    tabelas_especificas = {
        "PCESP": PATENTES_PCESP,
        "GER": PATENTES_GER,
        "DEIC": PATENTES_DEIC,
        "DHPP": PATENTES_DHPP,
        "GARRA": PATENTES_GARRA,
        "DOPE": PATENTES_DOPE
    }

    if companhia in tabelas_especificas:
        return tabelas_especificas[companhia]

    # 3 — Caso não seja nenhuma das acima → usa tabela PM normal
    return PATENTES
   

class TicketView(View):
    @discord.ui.button(label="Solicitar Funcional", style=discord.ButtonStyle.secondary, custom_id="iniciar_pedido")
    async def abrir_ticket(self, interaction: discord.Interaction, button: Button):
        guild = interaction.guild
        user = interaction.user

        if interaction.user.id in solicitacoes_abertas:
            await interaction.response.send_message("⚠️ Você já possui um ticket aberto.", ephemeral=True)
            return

        category = discord.utils.get(guild.categories, id=CATEGORIA_TICKET_ID)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        }
        canal = await guild.create_text_channel(name=f"ticket-{user.name}", category=category, overwrites=overwrites)
        solicitacoes_abertas[user.id] = {"canal_id": canal.id}

        view = View(timeout=None)
        view.add_item(SelectCompanhia(user.id))
        await canal.send(f"{user.mention}, selecione sua companhia:", view=view)
        await interaction.response.send_message("🎟️ Ticket criado! Verifique o canal criado.", ephemeral=True)
        await asyncio.sleep(5)
        try:
            await interaction.delete_original_response()
        except:
            pass

class SelectCompanhia(Select):
    def __init__(self, user_id):
        self.user_id = user_id
        options = [discord.SelectOption(label=nome, value=nome) for nome in COMPANHIAS_CHANNEL]
        super().__init__(placeholder="Escolha sua companhia", options=options, custom_id="select_companhia")

    async def callback(self, interaction: discord.Interaction):
        companhia = self.values[0]
        patentes = get_patentes_para(companhia)

        view = View(timeout=None)
        view.add_item(SelectPatente(self.user_id, companhia, patentes))
        await interaction.response.send_message(f"Companhia **{companhia}** selecionada. Agora selecione sua patente:", view=view, ephemeral=True)

class SelectPatente(Select):
    def __init__(self, user_id, companhia, patentes):
        self.user_id = user_id
        self.companhia = companhia
        self.patentes = patentes
        options = [discord.SelectOption(label=nome, value=nome) for nome in patentes]
        super().__init__(placeholder="Escolha sua patente", options=options, custom_id="select_patente")

    async def callback(self, interaction: discord.Interaction):
        patente_nome = self.values[0]
        patente_id = self.patentes[patente_nome]
        companhia_id = CARGOS_COMPANHIA[self.companhia]
        await interaction.response.send_modal(DadosPessoaisModal(self.user_id, self.companhia, patente_nome, patente_id, companhia_id))

class DadosPessoaisModal(Modal, title="Informe seus dados"):
    nome = TextInput(label="Nome Completo", required=True, max_length=80)
    passaporte = TextInput(label="Passaporte", required=True, max_length=20)

    def __init__(self, user_id, companhia, patente_nome, patente_id, companhia_id):
        super().__init__()
        self.user_id = user_id
        self.companhia = companhia
        self.patente_nome = patente_nome
        self.patente_id = patente_id
        self.companhia_id = companhia_id

    async def on_submit(self, interaction: discord.Interaction):
        nome = self.nome.value.strip()
        passaporte = self.passaporte.value.strip()
        solicitacoes_abertas[self.user_id].update({
            "patente_id": self.patente_id,
            "companhia_id": self.companhia_id,
            "nome": nome,
            "passaporte": passaporte
        })

        embed = Embed(title="Solicitar Funcional",
                      description=f"**Nome:** {nome}\n**Passaporte:** {passaporte}\n**Companhia:** {self.companhia}\n**Patente:** {self.patente_nome}",
                      color=discord.Color.dark_gray())
        embed.set_footer(text=f"Solicitante: {interaction.user}", icon_url=interaction.user.display_avatar.url)

        canal_logs = bot.get_channel(COMPANHIAS_CHANNEL[self.companhia])
        await canal_logs.send(embed=embed, view=ConfirmarOuFecharView(self.user_id))
        await interaction.response.send_message("✅ Solicitação enviada para avaliação.", ephemeral=True)

class ConfirmarOuFecharView(View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id

    @discord.ui.button(label="✅ Confirmar SET", style=discord.ButtonStyle.success)
    async def confirmar(self, interaction: discord.Interaction, button: Button):
        dados = solicitacoes_abertas.pop(self.user_id, None)
        if not dados:
            await interaction.response.send_message("❌ Solicitação não encontrada.", ephemeral=True)
            return

        membro = interaction.guild.get_member(self.user_id)
        novo_apelido = f"#{dados['passaporte']} | {dados['nome']}"


        try:
            await membro.edit(nick=novo_apelido)
        except:
            pass

        novato = interaction.guild.get_role(CARGO_NOVATO_ID)
        if novato in membro.roles:
            await membro.remove_roles(novato)

        await membro.add_roles(
            interaction.guild.get_role(dados['patente_id']),
            interaction.guild.get_role(dados['companhia_id'])
        )


        await interaction.response.send_message(f"✅ SET confirmado. Nick alterado para **{novo_apelido}**.", ephemeral=True)
        
        # Fecha o canal do ticket
        canal = bot.get_channel(dados['canal_id'])
        if canal:
            await asyncio.sleep(5)
            await canal.delete()

    @discord.ui.button(label="❌ Fechar Solicitação", style=discord.ButtonStyle.danger)
    async def fechar(self, interaction: discord.Interaction, button: Button):
        dados = solicitacoes_abertas.pop(self.user_id, None)
        await interaction.response.send_message("🗑️ Solicitação cancelada.", ephemeral=True)

        if dados:
            canal = bot.get_channel(dados['canal_id'])
            if canal:
                await asyncio.sleep(5)
                await canal.delete()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    canal = bot.get_channel(CANALETA_SOLICITAR_SET_ID)
    async for msg in canal.history(limit=10):
        if msg.author == bot.user:
            await msg.delete()
    await canal.send(embed=Embed(
        title="Segurança Pública | Solicitar Funcional",
        description="Clique no botão abaixo para iniciar sua solicitação de funcional.",
        color=discord.Color.dark_gray()
    ), view=TicketView())

@bot.event
async def on_member_join(member):
    novato_role = member.guild.get_role(CARGO_NOVATO_ID)
    if novato_role:
        try:
            await member.add_roles(novato_role, reason="Novo membro entrou no servidor.")
            print(f"Cargo de novato atribuído a {member.name}")
        except discord.Forbidden:
            print(f"Permissão negada ao tentar dar cargo de novato a {member.name}")
        except discord.HTTPException as e:
            print(f"Erro ao atribuir cargo de novato: {e}")


bot.run(TOKEN)