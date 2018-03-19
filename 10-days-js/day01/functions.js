
/*
 * Create the function factorial here
 */
function factorial(n){
    if (n > 1){
        return (n * factorial(n-1));
    } else{
        return 1;
    }
}