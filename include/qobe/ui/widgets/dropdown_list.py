
class DropdownListWidget:
    def __init__(self, alist):
        return self.write_html(alist)

    def write_html(self, alist):
        html = format('<div class="select" tabindex="0"><span class="value">{0}</span><ul class="optList">', alist.index(0))
        for item in self.alist:
            html += format('<li class="option">{0}</li>', item)
        html += '</ul></div>'
        return html

