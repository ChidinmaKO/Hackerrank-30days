	this.insert=function(head,data){
          //complete this method
        let node = new Node(data);
        if (head === null){
            head = node;
        } else{
            let currentNode = head;
            while (currentNode.next){
                currentNode = currentNode.next;
            }
            currentNode.next = node;
        }
        return head;
    };
