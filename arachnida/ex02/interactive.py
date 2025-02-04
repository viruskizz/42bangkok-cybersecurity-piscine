"""
Scorpion Interactive UI
"""

import sys
import os

from itertools import cycle
from textual import log
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.binding import Binding
from textual.widgets import DataTable, Header, Footer, Input, Button, Select

from PIL import Image, ExifTags

#####
### EXIF Operation Part
#####

class ExifImage:
    """ ExifImage """
    EXTENSIONS = [".heif", ".tiff", ".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    EXIF_TAGS = {
        **{i.value: i.name for i in ExifTags.LightSource},
        **ExifTags.GPSTAGS,
        **ExifTags.TAGS
    }

    def __init__(self, filename):
        self.filename = filename
        self.img = Image.open(filename)
        self.exif_data = self.img.getexif()


    def data_to_rows(self):
        """" Convert data to data table """
        rows = []
        for key, val in self.exif_data.items():
            if key in self.EXIF_TAGS:
                print(f'{self.EXIF_TAGS[key]}:\t{val}')
                rows.append((key, self.EXIF_TAGS[key], val))
        return rows

    def find(self, tagname):
        """
        Find valid EXIF tags read more:
        https://exiftool.org/TagNames/EXIF.html
        """
        for code,name in self.EXIF_TAGS.items():
            if tagname == name:
                return code

    def add(self, key, value):
        """ Add metadata key and value to EXIF """
        code = self.find(key)
        if code:
            self.exif_data[code] = value
            return code

    def delete(self, key):
        """" Delete metadata key from EXIF """
        code = self.find(key)
        if code in self.exif_data:
            del self.exif_data[code]

    def save(self):
        """ Save current metadata replace to file """
        self.img.convert('RGB').save(self.filename, 'JPEG', exif=self.exif_data)

class TableApp(App):
    CURSORS = "row"
    rows = []
    columns = ("code", "key", "value")
    CSS = """
    Horizontal {
        margin: 1
    }
    Select {
        width: 40%;
        margin: -1;
        padding-right: -1
    }
    Input {
        width: 40%;
    }
    Button {
        width: 20%
    }
    """
    BINDINGS = [
        Binding(key="d", action="delete", description="delete selected row"),
        Binding(key="r", action="refesh", description="refresh metadata"),
        Binding(key="s", action="save", description="save metadata to file"),
    ]
    exif_image: ExifImage

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Header()
        yield Footer()
        yield Horizontal(
            Select((v, v) for k, v in ExifImage.EXIF_TAGS.items()),
            Input(placeholder="value", id="value", type="text"),
            Button("Submit", variant="primary", classes="btn"),
        )


    def on_mount(self) -> None:
        self.title = "Scorpion Interactive Mode"
        self.sub_title = self.exif_image.filename
        self.rows = self.exif_image.data_to_rows()

        table = self.query_one(DataTable)
        table.cursor_type = self.CURSORS
        table.zebra_stripes = True
        for col in self.columns:
            table.add_column(col, key=col)
        table.add_rows(self.rows)

    def key_d(self):
        table = self.query_one(DataTable)
        row_key, _ = table.coordinate_to_cell_key(table.cursor_coordinate)
        row_data = table.get_row(row_key)
        metadata_key = row_data[1]
        table.remove_row(row_key)
        self.exif_image.delete(metadata_key)
        self.notify(f"Deleted: {metadata_key}", severity="error", timeout=2)

    def key_r(self):
        table = self.query_one(DataTable)
        table.clear()
        self.rows = self.exif_image.data_to_rows()
        table.add_rows(self.rows)
        table.sort("code")

    def key_s(self):
        self.exif_image.save()
        self.notify("Saved", severity="success", timeout=2)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        ipt = self.query_one(Input)
        select = self.query_one(Select)
        metadata_key = select.value
        metadata_val = ipt.value
        if metadata_key != select.BLANK and metadata_val:
            code = self.exif_image.add(metadata_key, metadata_val)
            table = self.query_one(DataTable)
            table.add_rows([(code, metadata_key, metadata_val)])
            self.notify(f"Added: {metadata_key}", timeout=2)
        else:
            self.notify("Metadata Key and Value could not empty", severity="error", timeout=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need file input")
        sys.exit(1)
    file = sys.argv[1]
    if os.path.splitext(file)[1] not in ExifImage.EXTENSIONS:
        print("INVALID FILE EXTENSION")
        sys.exit(1)
    app = TableApp()
    app.exif_image = ExifImage(file)
    app.run()
