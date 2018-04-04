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
    a = readLine().split(' ');
    a = a.map(Number);
    // Write Your Code Here
    let swapped;
    let numSwaps = 0;

    do{
        swapped = false;
        for(let i = 0; i < n - 1; i++){
            if(a[i] > a[i + 1]){
                let temp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = temp;
                swapped = true;
                numSwaps++;
            }
        }
    } while(swapped === true);
        console.log("Array is sorted in " + numSwaps + " swaps.");
        console.log("First Element: " + a[0]);
        console.log("Last Element: " + a[n-1]);

}
