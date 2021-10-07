class SLLNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}


class SLList {
    constructor() {
        this.head = null;
    }

    addToFront(value) {
        var newNode = new SLLNode(value);

        newNode.next = this.head;
        this.head = newNode;
    }

    // given a value, add it to the back of your singly linked list
    // what if the list is empty?
    addToBack(value) {
        var newNode = new SLLNode(value);

        if (this.head == null) {
            this.head = newNode;
            return;
        }

        var runner = this.head;

        while (runner.next != null) {
            // console.log(runner.value)
            runner = runner.next;
        }
        runner.next = newNode;
    }

    // print the singly linked list
    printValues() {
        if (this.head == null) {
            console.log("Nothing in list!");
        } else {
            var runner = this.head;
            var str = "";

            while (runner != null) {
                str += runner.value
                console.log("the current value is:", runner.value)
                runner = runner.next;
            }
            console.log(str);
        }
    }

    // given a value, traverse through your list and return true or false if the value exists in the list
    contains(value) {
        // edge case: what if there's nothing in the list?
        if (!this.head) { //this.head === null
            console.log("There's nothing in this list, so it cannot contain anything!")
            return false
        }
        // start runner at the beginning of the list
        var runner = this.head;
        while (runner != null) {
            // check if the input value is equal to the runner's value
            if (runner.value == value) {
                // if it is, return true
                // console.log(`Found it! ${runner.value}`);
                return true
            }
            runner = runner.next;
        }
        // if we made it through out entire list and never hit true, we didn't find it!
        return false
    }

    removeFromFront() {
        if (this.head != null) {
            var removedNode = this.head;
            this.head = this.head.next;
            removedNode.next = null;
        }
    }

    removeFromFront() {
        if (this.head != null) {
            var removedNode = this.head;
            this.head = this.head.next;
            removedNode.next = null;
        }
    }

    moveMinToFront() {
        if (this.head == null || this.head.next == null) {
            console.log("List is too short! Cannot move to front")
            // return 'this' to end function and allow chaining of methods
            return this
        }
        var runner = this.head
        var minNode = this.head
        var firstNode = this.head
        console.log("the minNode is", minNode)
        while (runner.next != null) {

            if (runner.value < minNode.value) {
                minNode.value = runner.value
            }
            runner = runner.next
        }
        return minNode

        removeFromBack() {
            // this handles 2 edge cases: nothing in list, and only 1 item in list
            if (this.head == null || this.head.next == null) {
                console.log("List is too short! Cannot remove from back")
                // return 'this' to end function and allow chaining of methods
                return this
            }
            // ** alternate edge case handling, handles if there is only 1 items in the list or no items separately
            // if(this.head == null) {
            //     console.log("Nothing in the list! Cannot remove from back")
            //     return this
            // }
            // if(this.head.next == null) {
            //     this.head = null
            //     return this
            // }
            // set runner to start at the beginning of list
            var runner = this.head;

            // run all the way through this list until you hit the second to last item and stop
            while (runner.next.next != null) {
                runner = runner.next
            }
            // set runner.next to null, effectively removing final node from the list
            runner.next = null;
            return this
        }
    }

    const SLL = new SLList();
    SLL.addToBack(1)
    SLL.addToBack(2)
    SLL.addToBack(3)
    SLL.addToBack(4)
    SLL.addToBack(5)
    SLL.addToBack(6)
    SLL.addToBack(7)
    // SLL.printValues()

    // SLL.removeFromBack();
    SLL.printValues();


    SLL.removeFromBack();

// SLL.contains(3);