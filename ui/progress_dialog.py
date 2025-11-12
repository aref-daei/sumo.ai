import customtkinter as ctk


class ProgressDialog(ctk.CTkToplevel):
    """Progress display window"""

    def __init__(self, parent, title="Processing ..."):
        super().__init__(parent)

        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)

        # Block the main window
        self.transient(parent)
        self.grab_set()

        # Place in the middle of the page
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.winfo_screenheight() // 2) - (200 // 2)
        self.geometry(f"400x200+{x}+{y}")

        self.setup_ui()

    def setup_ui(self):
        """UI construction"""

        self.message_label = ctk.CTkLabel(
            self,
            text="Please wait ...",
            font=ctk.CTkFont(size=14)
        )
        self.message_label.pack(pady=30)

        self.progress_bar = ctk.CTkProgressBar(self, width=350)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

        self.detail_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.detail_label.pack(pady=10)

    def update_progress(self, progress: float, message: str = None, detail: str = None):
        """Progress update"""
        self.progress_bar.set(progress)

        if message:
            self.message_label.configure(text=message)

        if detail:
            self.detail_label.configure(text=detail)

        self.update()
