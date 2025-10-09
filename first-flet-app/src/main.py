import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas"
    page.padding = 100

    caixaDeTexto = ft.TextField(width=300)
    vetCheckbox = []
    vetRow = []  

    def abre_editar(indice, e):
        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Editando:"),
            content=ft.TextField(width=20, value=vetCheckbox[int(indice)].label),       
            actions_alignment=ft.MainAxisAlignment.END,
            actions=[
                ft.TextButton("Editar", on_click=lambda e: editar(int(indice), dlg_modal, e)),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg_modal)),
            ],
            on_dismiss=lambda e: print("Fechando PopUp!")
        )
        page.open(dlg_modal)



    def editar(indice, modal, e):        
        vetCheckbox[int(indice)].label = modal.content.value
        page.close(modal)
        page.update()

    def checkbox_changed(indice, e):
        pass
        # if vetCheckbox[int(indice)].value is True:
        # page.add(ft.Text(f"Checkbox {indice} value changed to {vetCheckbox[int(indice)].value}"))
        # page.update()

    def remover(indice, e):
        vetRow[int(indice)].visible = False
        page.update()


    def adicionar(e):
        indice = int(len(vetCheckbox))
        checkbox = ft.Checkbox(on_change=lambda e: checkbox_changed(indice, e))
        checkbox.value = False
        checkbox.label = caixaDeTexto.value
        caixaDeTexto.value = ""
        vetCheckbox.append(checkbox)
        vetRow.append(ft.Row([checkbox, ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e: remover(indice, e)), ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e: abre_editar(indice, e))]))
        page.add(vetRow[-1])       


    botaoAdicionar = ft.ElevatedButton(
        "Adicionar",
        on_click=adicionar
    )

    page.add(caixaDeTexto)
    page.add(botaoAdicionar)



ft.app(main)
