import {ul, button, a, i, li, h4, form, input, div} from 'charata'

export default class TodoList {
    constructor(list = []) {
        this.list = {}
        list.forEach(el => addItem(el))
    }

    addItem(text) {
        let idx = Date.now()    // id of the element
        this.list[idx] = text
        this.render()
    }

    removeItem(idx) {
        delete this.list[idx]
        this.render()
    }

    _attachEvents() {
        let done_anchors = this.container.getElementsByTagName('a')
        Array.prototype.forEach.call(done_anchors, anchor => {
            anchor.addEventListener('click', ev => {
                ev.preventDefault()
                let idx = anchor.parentElement.parentElement.dataset.idx
                this.removeItem(idx)
            })
        })
    }

    _renderItems() {
        return Object.keys(this.list).map(idx => {
            return li(
                div([
                    this.list[idx],
                    a(i('send', null, ['class', 'material-icons']), null, ['class', 'secondary-content', 'href', '#!'])
                ]), idx, ['data-idx', idx, 'class', 'collection-item'])
        })
    }

    render(container) {
        this.container = container || this.container || document.body
        let items = this._renderItems()
        if (items.length) {
            ul(items, null, ['class', 'collection']).renderTo(this.container)
        }
        else {
            div('Hooray! You are free!', null, ['class', 'center']).renderTo(this.container)
        }
        this._attachEvents()
    }
}