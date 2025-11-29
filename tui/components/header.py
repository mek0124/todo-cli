from textual.widgets import Header


class CustomHeader(Header):
    def __init__(
        self,
        show_clock=False,
        name=None,
        id=None,
        classes=None,
        icon="",
        time_format=None,
        tall=False,
        screen_sub_title=None,
        screen_title=None,
        **kwargs
    ):
        super().__init__(
            show_clock=show_clock,
            name=name,
            id=id,
            classes=classes,
            icon=icon,
            time_format=time_format,
            **kwargs
        )
        self.sub_title = screen_sub_title
        self.title = screen_title
        self.tall = tall