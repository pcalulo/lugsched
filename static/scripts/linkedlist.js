
/*
 * A linked list implementation intended for use in clicklists
 */

function LinkedListNode(data) {
	this.data = data;
	this.next = null;
}

function LinkedList() {
	this.first = null;
	this.last = null;
	this.sortFunc = null;
	this.length = 0;
}

LinkedList.prototype.isEmpty = function() {
	return this.length == 0;
}

LinkedList.prototype.addNode = function(node) {
	if (this.last) {
		// The list isn't empty, add the node to the end of the list
		this.last.next = node;
		this.last = node;
	} else {
		// The list is empty, this is our first node
		this.first = node;
		this.last = node;
	}
	this.length++;
}

LinkedList.prototype.add = function(data) {
	var node = new LinkedListNode(data);
	this.addNode(node);
}

// "sortFunc" should behave like strcmp. See "man strcmp".
LinkedList.prototype.setSortFunction = function(sortFunc) {
	this.sortFunc = sortFunc;	
}

LinkedList.prototype.orderedAddNode = function(node) {
	var cur, prev, result;
	var inserted = false;
	var insertIndex = 0;

	if (!this.sortFunc) {
		console.error("orderedAddNode called without setting a sortFunc");
		return;
	}
	
	if (!this.first) {
		this.first = node;
		this.last = node;
		this.length++;
		return;
	}

	cur = this.first;
	prev = null;
	while (cur && !inserted) {
		result = this.sortFunc(node.data, cur.data);
		if (result < 0) {
			if (!prev) {
				this.first = node;
				node.next = cur;
			} else {
				prev.next = node;
				node.next = cur;
			}
			inserted = true;
			this.length++;
		}
		insertIndex++;
		prev = cur;
		cur = cur.next;
	}

	if (!inserted) {
		// If the loop finishes without inserting, "prev" will be left pointing
		// at the last node
		prev.next = node;
	}
	this.length++;
}

LinkedList.prototype.orderedAdd = function(data) {
	var node = new LinkedListNode(data);
	this.orderedAddNode(node);
}

LinkedList.prototype.removeNode = function(node) {
	var cur = this.first;
	var prev = null;

	if (node == this.first) {
		this.first = cur.next;
		this.length--;
		return;
	}

	while (cur) {
		if (cur == node) {
			prev.next = cur.next;
			this.length--;
			break;
		}
		prev = cur;
		cur = cur.next;
	}

	// "prev" will point at the last element after the loop runs
	this.last = prev;
}

LinkedList.prototype.removeVal = function(data, cmpFunc) {
	var cur = this.first;
	var prev = this.first;

	if (!cmpFunc) {
		cmpFunc = function(a,b) { return a == b; };
	}

	if (cmpFunc(this.first.data, data)) {
		this.first = cur.next;
		this.length--;
		if (this.length == 0) {
			this.last = null;
		}
		return;
	}

	while (cur) {
		var match = false;
		if (cmpFunc(cur.data, data)) {
			prev.next = cur.next;
			match = true;
			this.length--;
		}

		// Do not advance prev to a just-deleted node
		if (!match)
			prev = cur;
		cur = cur.next;
	}

	// "prev" will point at the last element after the loop runs
	this.last = prev;
}


/*
 * The "extra" argument allows the caller to supply additional data
 * to funcToRun
 */
LinkedList.prototype.traverse = function(funcToRun, extra) {
	var cur = this.first;

	if (!funcToRun) {
		funcToRun = function(x) { console.log(x) };
	}

	while (cur) {
		funcToRun(cur.data, extra);
		cur = cur.next;
	}
}

