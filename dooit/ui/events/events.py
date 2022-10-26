from typing import Literal
from rich.console import RenderableType
from textual.widgets import NodeID
from textual.message import Message, MessageTarget

StatusType = Literal["NORMAL", "INSERT", "DATE", "SEARCH", "SORT"]
SortMethodType = Literal["name", "status", "date", "urgency"]


class MenuOptionChange(Message, bubble=True):
    """
    Emitted when user moves through nav menu
    """

    def __init__(self, sender: MessageTarget, option: str) -> None:
        super().__init__(sender)
        self.option = option


class ChangeStatus(Message, bubble=True):
    """
    Emitted when there is a change in the `status`
    See: StatusType
    """

    def __init__(self, sender: MessageTarget, status: StatusType) -> None:
        super().__init__(sender)
        self.status = status


class Notify(Message, bubble=True):
    """
    Emitted when A notification message on status bar is to be shown
    """

    def __init__(self, sender: MessageTarget, message: RenderableType) -> None:
        super().__init__(sender)
        self.message = message


class ModifyTopic(Message, bubble=True):
    """
    Emitted when a nav top is renamed
    """

    def __init__(self, sender: MessageTarget, old: str, new: str) -> None:
        super().__init__(sender)
        self.old = old
        self.new = new


class ApplySortMethod(Message, bubble=True):
    """
    Emitted when the user selects a sort method from sort-menu
    """

    def __init__(self, sender: MessageTarget, method: str) -> None:
        super().__init__(sender)
        self.method = method


class HighlightNode(Message, bubble=True):
    """
    Emitted when the user selects a todo from search list
    """

    def __init__(self, sender: MessageTarget, id: NodeID) -> None:
        super().__init__(sender)
        self.id = id


class TopicSelect(Message, bubble=True):
    """
    Emitted when the user selects a todo from search list
    """

    def __init__(self, sender: MessageTarget, item) -> None:
        super().__init__(sender)
        self.item = item


class SwitchTab(Message, bubble=True):
    """
    Emitted when user presses `Esc` while in normal mode in todo
    """

    pass


class RemoveTopic(Message, bubble=True):
    """
    Emitted when user presses `Esc` while in normal mode in todo
    """

    def __init__(self, sender: MessageTarget, selected: str) -> None:
        super().__init__(sender)
        self.selected = selected
