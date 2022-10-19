// Best time to buy and Sell stock

// O(N)
// Kadane's algorithm
int maxSubArraySum(vector<int> &arr) {
    int sum = 0, maxSum = 0; 
    for(int i=0; i<arr.size(); i++) {
        sum += arr[i];
        if(sum < 0) sum = 0;
        if(sum > maxSum) maxSum = sum;
    }
    return maxSum;
}

// prices[4] - prices[1] => prices[4]-prices[3] + prices[3]-prices[2] + prices[2]-prices[1]
                      // => arr[4] + arr[3] + arr[2]  which is Maximum subarray sum
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    vector<int> arr(n);
    arr[0] = 0;
    for(int i=1; i<n; i++) {
        arr[i] = prices[i] - prices[i-1];
    }
    return maxSubArraySum(arr);
}


// Another Approach => O(N)
int maxProfit(vector<int>& prices) {
    int maxProf = 0, minPrice = 1e9;

    for(int i=0; i<prices.size(); i++) {
        minPrice = min(minPrice, prices[i]);
        maxProf = max(maxProf, prices[i]-minPrice);
    }
    return maxProf;
}
