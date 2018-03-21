/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    var largest = Math.max(...nums);
    var largestIndex = nums.indexOf(largest);
    nums[largestIndex] = -Infinity;

    while(largest == Math.max(...nums)){
        var largest = Math.max(...nums);
        var largestIndex = nums.indexOf(largest);
        nums[largestIndex] = -Infinity;
    }

    // returning the second maximum value
    return Math.max(...nums);


}