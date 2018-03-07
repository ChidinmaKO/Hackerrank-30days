
function processData(input) {
    input = input.split("\n");

    for (var i = 1; i < input.length; i++){
        var z = input[i].split('');

        var even = '';
        var odd = '';

        for (var j = 0; j < z.length; j++){
            if (j % 2 === 0){
                even = even + z[j];
            } else {
                odd = odd + z[j];
            }
        }
        console.log (even + " " + odd);
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
