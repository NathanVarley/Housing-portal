import flet as ft
import time

def main(page: ft.Page):
    page.title = "Aegis Wellness Engine"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # --- GROUNDING EXERCISE COMPONENT ---
    def start_grounding(e):
        page.clean()
        pulse = ft.Container(
            width=100, height=100,
            bgcolor=ft.colors.BLUE_200,
            border_radius=50,
            animate=ft.animation.Animation(2000, ft.AnimationCurve.EASE_IN_OUT)
        )
        page.add(
            ft.Text("Breathe... Expand...", size=20),
            ft.Container(content=pulse, alignment=ft.alignment.center, height=400),
            ft.ElevatedButton("Back to Dashboard", on_click=lambda _: main(page))
        )
        # Pulse animation simulation
        for _ in range(5):
            pulse.width, pulse.height = 250, 250
            page.update()
            time.sleep(2)
            pulse.width, pulse.height = 100, 100
            page.update()
            time.sleep(2)

    # --- MAIN DASHBOARD ---
    def show_dashboard():
        page.clean()
        page.add(
            ft.Text("CORE COMPANION", size=30, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.ElevatedButton("Start Grounding Exercise", icon=ft.icons.FILTER_CENTER_FOCUS, on_click=start_grounding),
            ft.ElevatedButton("View Local Support Resources", icon=ft.icons.MAP, on_click=lambda _: show_resources()),
            ft.ElevatedButton("AI Support Chat", icon=ft.icons.CHAT, on_click=lambda _: show_chat())
        )

    # --- RESOURCES SCREEN ---
    def show_resources():
        page.clean()
        page.add(
            ft.Text("Non-Confinement Centers", size=24),
            ft.ListView(controls=[
                ft.ListTile(leading=ft.Icon(ft.icons.LOCATION_ON), title=ft.Text("Wellness Hub Alpha"), subtitle=ft.Text("0.5 miles")),
                ft.ListTile(leading=ft.Icon(ft.icons.LOCATION_ON), title=ft.Text("Peer Support Collective"), subtitle=ft.Text("1.2 miles")),
            ], height=300),
            ft.ElevatedButton("Back", on_click=lambda _: show_dashboard())
        )

    # --- CHAT INTERFACE ---
    def show_chat():
        page.clean()
        chat_display = ft.Column([], scroll=ft.ScrollMode.AUTO, height=400)
        input_field = ft.TextField(hint_text="Speak freely...")
        
        page.add(
            chat_display,
            input_field,
            ft.IconButton(ft.icons.SEND, on_click=lambda e: chat_display.controls.append(ft.Text(f"You: {input_field.value}")) or page.update()),
            ft.ElevatedButton("Back", on_click=lambda _: show_dashboard())
        )

    show_dashboard()

ft.app(target=main)
