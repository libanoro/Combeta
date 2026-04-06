import customtkinter as ctk
from tkinter import messagebox

# Configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CombetaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("COMBETA VERSÃO 2.0 - Planejamento de Voo")
        self.geometry("500x700")
        self.resizable(False, False)

        # Banco de dados das aeronaves
        self.aeronaves = {
            "Airbus A320": {
                "consumo": 2700, "mzfw": 62500, "boew": 42400,
                "mtow": 77000, "mlw": 66000, "tanque": 24325
            },
            "Boeing B737": {
                "consumo": 2550, "mzfw": 61700, "boew": 41400,
                "mtow": 79000, "mlw": 65300, "tanque": 20800
            }
        }

        self.setup_ui()

    def setup_ui(self):
        # Título
        self.lbl_titulo = ctk.CTkLabel(self, text="COMBETA 2.0", font=("Roboto", 24, "bold"))
        self.lbl_titulo.pack(pady=(20, 5))

        self.lbl_subtitulo = ctk.CTkLabel(self, text="Desenvolvido por: Tiago A L de Oliveira", font=("Roboto", 12))
        self.lbl_subtitulo.pack(pady=(0, 20))

        # --- Frames de Entrada ---
        self.frame_inputs = ctk.CTkFrame(self)
        self.frame_inputs.pack(padx=20, pady=10, fill="x")

        # Seleção de Aeronave
        ctk.CTkLabel(self.frame_inputs, text="Selecione a Aeronave:").pack(pady=(10, 0))
        self.combo_aviao = ctk.CTkOptionMenu(self.frame_inputs, values=list(self.aeronaves.keys()))
        self.combo_aviao.pack(pady=5)

        # Payload
        ctk.CTkLabel(self.frame_inputs, text="Carga a bordo (Payload em Kg):").pack(pady=(10, 0))
        self.ent_payload = ctk.CTkEntry(self.frame_inputs, placeholder_text="Ex: 15000")
        self.ent_payload.pack(pady=5)

        # Tempo de Voo
        ctk.CTkLabel(self.frame_inputs, text="Tempo de voo previsto (Horas decimais):").pack(pady=(10, 0))
        self.ent_tempo = ctk.CTkEntry(self.frame_inputs, placeholder_text="Ex: 1.5")
        self.ent_tempo.pack(pady=5)

        # Tempo Alternativo
        ctk.CTkLabel(self.frame_inputs, text="Tempo para aeroporto alternativo (Minutos):").pack(pady=(10, 0))
        self.ent_alt = ctk.CTkEntry(self.frame_inputs, placeholder_text="Ex: 30")
        self.ent_alt.pack(pady=5)

        # Botão Calcular
        self.btn_calcular = ctk.CTkButton(self, text="CALCULAR RELATÓRIO", command=self.calcular,
                                          font=("Roboto", 14, "bold"))
        self.btn_calcular.pack(pady=20)

        # --- Frame de Resultados ---
        self.frame_res = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_res.pack(padx=20, pady=10, fill="both", expand=True)

        self.txt_resultado = ctk.CTkTextbox(self.frame_res, font=("Courier New", 13), state="disabled")
        self.txt_resultado.pack(fill="both", expand=True)

    def calcular(self):
        try:
            # Captura e validação de dados
            nome_aviao = self.combo_aviao.get()
            dados = self.aeronaves[nome_aviao]

            payload = float(self.ent_payload.get().replace(',', '.'))
            horas_voo = float(self.ent_tempo.get().replace(',', '.'))
            min_alternativo = float(self.ent_alt.get().replace(',', '.'))

            # Lógica de Cálculo (Mantendo a sua original)
            consumo_hora = dados['consumo']
            comb_trecho = horas_voo * consumo_hora * 1.1
            comb_alternativo = (min_alternativo / 60) * consumo_hora
            comb_reserva = (45 / 60) * consumo_hora
            taxi = 200

            comb_total = comb_trecho + comb_alternativo + comb_reserva + taxi
            mfod = comb_alternativo + comb_reserva

            zfw = dados['boew'] + payload
            tow = comb_trecho + zfw + mfod
            ppp = zfw + mfod
            autonomia = (horas_voo * 60 + min_alternativo + 45 + 5) / 60

            # Verificações
            check_tow = "✅ SIM" if tow <= dados['mtow'] else "❌ ATENÇÃO!!!"
            check_ppp = "✅ SIM" if ppp <= dados['mlw'] else "❌ ATENÇÃO!!!"
            check_zfw = "✅ SIM" if zfw <= dados['mzfw'] else "❌ ATENÇÃO!!!"

            # Formatação do Relatório
            relatorio = f"""=== RELATÓRIO: {nome_aviao} ===

Combustível Total: {comb_total:.2f} Kg
ZFW (Peso sem Comb): {zfw:.2f} Kg
TOW (Peso Decolagem): {tow:.2f} Kg
Autonomia Estimada: {autonomia:.2f} h

--- PADRÕES DE VERIFICAÇÃO ---
TOW < MTOW ({dados['mtow']}): {check_tow}
PPP < MLW  ({dados['mlw']}): {check_ppp}
ZFW < MZFW ({dados['mzfw']}): {check_zfw}
------------------------------"""

            # Exibição no Textbox
            self.txt_resultado.configure(state="normal")
            self.txt_resultado.delete("1.0", "end")
            self.txt_resultado.insert("1.0", relatorio)
            self.txt_resultado.configure(state="disabled")

        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números válidos nos campos.")


if __name__ == "__main__":
    app = CombetaApp()
    app.mainloop()