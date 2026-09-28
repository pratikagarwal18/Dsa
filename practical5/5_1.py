class Song:
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.first = None
        self.last = None
        self.total = 0

    def add_to_start(self, title):
        song = Song(title)
        if self.first is None:
            self.first = song
            self.last = song
        else:
            song.next = self.first
            self.first.prev = song
            self.first = song
        self.total += 1

    def add_to_end(self, title):
        song = Song(title)
        if self.last is None:
            self.first = song
            self.last = song
        else:
            song.prev = self.last
            self.last.next = song
            self.last = song
        self.total += 1

    def add_after(self, current, title):
        node = self.first
        while node is not None and node.title != current:
            node = node.next

        if node is None:
            return False

        song = Song(title)
        song.prev = node
        song.next = node.next

        if node.next is not None:
            node.next.prev = song
        else:
            self.last = song

        node.next = song
        self.total += 1
        return True

    def remove_first(self):
        if self.first is None:
            return None

        removed = self.first.title
        self.first = self.first.next

        if self.first is None:
            self.last = None
        else:
            self.first.prev = None

        self.total -= 1
        return removed

    def count(self):
        return self.total

    def show(self):
        titles = []
        node = self.first
        while node is not None:
            titles.append(node.title)
            node = node.next
        return " <-> ".join(titles) if titles else "Playlist is empty"


def main():
    playlist = Playlist()

    operations = [
        ("add_to_end", "Believer"),
        ("add_to_start", "Faded"),
        ("add_to_end", "Closer"),
        ("add_after", "Believer", "Perfect"),
        ("add_after", "Closer", "Legends"),
        ("add_after", "Shape of You", "Senorita"),
        ("count",),
        ("remove_first",),
        ("show",),
        ("remove_first",),
        ("remove_first",),
        ("remove_first",),
        ("remove_first",),
        ("remove_first",),
        ("count",),
    ]

    for step, op in enumerate(operations, start=1):
        name = op[0]
        message = ""

        if name == "add_to_start":
            playlist.add_to_start(op[1])
            message = f"Added '{op[1]}' at the start"
        elif name == "add_to_end":
            playlist.add_to_end(op[1])
            message = f"Added '{op[1]}' at the end"
        elif name == "add_after":
            if playlist.add_after(op[1], op[2]):
                message = f"Added '{op[2]}' after '{op[1]}'"
            else:
                message = f"'{op[1]}' not found, nothing added"
        elif name == "remove_first":
            removed = playlist.remove_first()
            if removed:
                message = f"Removed '{removed}'"
            else:
                message = "Nothing to remove"
        elif name == "count":
            message = f"Total songs: {playlist.count()}"
        elif name == "show":
            message = "Showing playlist"

        print(f"{step}. {message}")
        print(f"   {playlist.show()}\n")


if __name__ == "__main__":
    main()