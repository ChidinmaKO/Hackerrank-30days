function processData(input) {
    //Enter your code here
    input = input.split('\n');
    var phonebook = [];
    var entry = parseInt(input[0]);

    for (var j = 1; j <= entry; j++){
        var contactArray = input[j].split(' ');
        phonebook[contactArray[0]] = contactArray[1];
    }

    for (var j = entry + 1; j < input.length; j++){
        var number = (phonebook[input[j]]);
        if (number !== undefined){
            console.log(input[j] +'='+ number);
        } else{
            console.log('Not found');
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
