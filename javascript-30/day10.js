process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function main() {
  var n = parseInt(readLine());
  var binary = [];

  while (n > 0) {
    binary.push(n % 2)
    n = Math.floor(n / 2)
  }

  binary = binary.reverse();

  var ones = 0;
  var max = 0;

  for (j = 0; j < binary.length; j++) {
    if (binary[j] === 1) {
      ones += 1;
    } else if (binary[j] === 0) {
      if (ones > max) max = ones;
      ones = 0;
    }
  }

  if (ones > max) max = ones;

  console.log(max);
}