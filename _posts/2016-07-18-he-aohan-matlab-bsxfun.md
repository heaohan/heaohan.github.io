---
layout: post
title: "Try to replace \"for\" with bsxfun in MATLAB"
date: 2016-07-18
---

Today I try to use ```bsxfun``` function to replace the time-consuming "for" loop in my matlab code. I try to figure out the way to describe the computation process in matrix. The trick lies on that we need focus on every row of the matrix result first. With help of several bsxfun, we could get ride of "for" completely. 
