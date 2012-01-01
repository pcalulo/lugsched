
/*
 * clicklist.js: a system for easily creating and manipulating 
 * lists of items
 */

function ClickListButtonData() {
	this.text = "";
	this.onClick = null;
}

function ClickListElement() {
	this.mainText = "";
	this.subText = "";
	this.rightText = "";
	this.button1 = new ClickListButtonData();
	this.button2 = new ClickListButtonData();
}

function ClickList(div) {
	this.div = div;
	this.list = new LinkedList();
	this.emptyText = "";
}

ClickList.prototype.updateEmptyText = function() {
	if (this.list.isEmpty()) {
		this.div.find(".clicklist-empty-text").show();
	} else {
		this.div.find(".clicklist-empty-text").hide();
	}
}

ClickList.prototype.setEmptyText = function(emptyText) {
	var textElem = this.div.find(".clicklist-empty-text");
	if (!textElem) {
		console.error("This ClickList has no empty text");
		return;
	}

	textElem.text(emptyText);
	this.updateEmptyText();
}

ClickList.prototype.setSortFunction = function(sortFunc) {
	this.list.setSortFunc(sortFunc);
}

ClickList.prototype.updateItems = function() {
	// Only the last element should have a bottom border, as having two
	// adjacent bottom borders results in a thick, ugly line
    // This also adds the rounded bottom border edges
	this.div.find(".clicklist-item-bottom").removeClass("clicklist-item-bottom");
	this.div.find(".clicklist-item:last").addClass("clicklist-item-bottom");

    // Only the top element should have rounded top edges
    this.div.find(".clicklist-item-top").removeClass("clicklist-item-top")
    this.div.find(".clicklist-item:first").addClass("clicklist-item-top")

	this.div.find(".clicklist-item").hover(function() {
		$(this).addClass("clicklist-item-hover");
	}, function() {
		$(this).removeClass("clicklist-item-hover");
	});
}

ClickList.prototype.orderedAdd = function(element) {
	this.list.orderedAdd(element);
}

ClickList.prototype.createItemHTML = function(element) {
	var html = "<div class='clicklist-item' id='clicklist-new'>" + 
	"<div class='clicklist-maintext'>" + element.mainText;  

	html += "<div class='clicklist-righttext'>" + element.rightText + "</div>"
	html += "</div>"
	if (element.button1.text) {
		html += "<input type='button' value='" + element.button1.text;
		html += "' class='clicklist-item-button'></input>";
	}

	if (element.button2.text) {
		html += "<input type='button' value='" + element.button2.text;
		html += "' class='clicklist-item-button'></input>";
	}

	html += "<div class='clicklist-subtext'>" + element.subText + "</div>";
	
		
	html += "</div>";
	return html;
}

ClickList.prototype.initListItem = function(item, data) {
	item.attr("mainText", data.mainText);
	item.find("input:first").click(data.button1.onClick);
	item.find("input:last").click(data.button2.onClick);
	item.attr("id", null);
}

ClickList.prototype.add = function(element) {
	if (!element.mainText) {
		console.error("Missing mainText");
		return;
	}
	this.list.add(element);
	this.div.append(this.createItemHTML(element));

	var newItem = $("#clicklist-new");
	this.initListItem(newItem, element);
	this.updateEmptyText();
	this.updateItems();

	// Return the DOM element, so effects can be applied if desired.
	return this.div.find(":eq(" + this.list.length + ")");
}


ClickList.prototype._fullUpdateTraversalFunc = function(element, list) {
	list.div.append(list.createItemHTML(element));
	list.initListItem($("#clicklist-new"), element);
}
/*
 * An easy but inefficient way to update the list
 */
ClickList.prototype.fullUpdate = function() {
	this.div.find(".clicklist-item").remove();	
	this.list.traverse(this._fullUpdateTraversalFunc, this);
	this.updateItems();
	this.updateEmptyText();
}

ClickList.prototype._rmCmpFunc = function(a, b) {
	var match = true;
	if (a.mainText && b.mainText && (a.mainText != b.mainText)) {
		match = false;
	}
	if (a.subText && b.subText && (a.subText != b.subText)) {
		match = false;
	}
	if (a.rightText && b.rightText && (a.rightText != b.rightText)) {
		match = false;
	}
	return match;
}

ClickList.prototype.remove = function(element) {
	this.list.removeVal(element, this._rmCmpFunc);
	this.fullUpdate();
}

ClickList.prototype.removeAll = function() {
	this.list = new LinkedList();
	this.fullUpdate();
}

