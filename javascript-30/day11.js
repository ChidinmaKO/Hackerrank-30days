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
    var arr = [];
    for(arr_i = 0; arr_i < 6; arr_i++){
       arr[arr_i] = readLine().split(' ');
       arr[arr_i] = arr[arr_i].map(Number);
    }

    var sumArray = [];
    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr[i].length; j++) {
            if (arr[i] && arr[i + 1] && arr[i + 2]) {
                if (arr[i][j + 1] != undefined && arr[i][j + 2] != undefined) {
                    sumArray.push(
                        arr[i][j] + arr[i][j+1] +
                        arr[i][j+2] + arr[i+1][j+1] +
                        arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        }
      }
    }
  }
  console.log(Math.max(...sumArray));
    //console.log(Math.max.apply(Math, sumArray));
    // could have used null or undefined instead of Math...
    //console.log(Math.max.apply(null, sumArray));

}
