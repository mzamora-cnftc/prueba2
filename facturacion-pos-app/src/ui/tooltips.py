def create_tooltip(widget, text):
    tooltip = None

    def show_tooltip(event):
        nonlocal tooltip
        tooltip = Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = Label(tooltip, text=text, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(event):
        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)