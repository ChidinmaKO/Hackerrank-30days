function Solution(){
  //Write your code here
    this.queue = [];
    this.stack = [];

    this.pushCharacter = this.stack.push;
    this.enqueueCharacter = this.queue.push;
    this.popCharacter = this.stack.pop;
    this.dequeueCharacter = this.queue.shift;
}