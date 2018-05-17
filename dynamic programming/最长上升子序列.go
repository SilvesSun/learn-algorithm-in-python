package main

import (
	"math"
	"fmt"
)

func LengthOfLIS(nums[] int) (res int)  {
	length := len(nums)
	dp := make([]int, length)
	// 初始化数组
	for i := 0; i < length; i++ {
		dp[i] = 1
	}

	for i := 1;i < length ; i ++  {
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] && dp[i] < dp[j] + 1 {
				dp[i] = dp[j] + 1
			}
		}
	}

	res = 0

	for _, v := range dp {
		res = int(math.Max(float64(res), float64(v)))
	}
	fmt.Println(res)
	return res

}

func main() {
	nums := [] int {1, 2, 3,5,6}
	LengthOfLIS(nums)
}