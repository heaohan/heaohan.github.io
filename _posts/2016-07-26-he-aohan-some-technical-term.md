---
layout: post
title: "Some Technical Terms"
date: 2016-07-26
---

###Spatial light modulator:

> Usually, an SLM modulates **the intensity of the light beam**. However, it is also possible to produce devices that modulate **the phase of the beam** or both the intensity and the phase simultaneously.

> SLMs have been used as a component in optical computing. They also often find application in **holographic optical tweezers**.

>Liquid crystal SLMs can help solve problems related to **laser microparticle manipulation**. In this case spiral beam parameters can be changed dynamically.

###spiral phase plate:

>旋光片

###four-quadrant inverse tangent:

>atan2

###矢量图

>用函数描述图像的图

###speckle decorrelation

>The random noise of the laser speckle field which develops at the focusing plane of an imaging system, is, by now, efficiently used in several interferometric techniques as an information carrier of the macroscopic wavefront distortion induced by the surface displacement field of the object under investigation. The actual noise in this kind of techniques is represented by the speckle decorrelation at the image plane — i.e. the destruction of the carrier — which may be caused by the modification of the texture surface (e.g. by yielding under a severe stress state), but it is inherently produced by the same displacement field under measurement.

###Bilinear interpolation

>双线性插值常用于图像的放大和缩小，相比最邻近插值，马赛克效应会减小。相应的公式为
![alt text](https://heaohan.github.io/files/2016-08-02_100647.jpg)

###randn和rand

>randn产生高斯随机信号，rand产生均匀分布信号。

###grating

>光栅

###principal value

对于复数域中多值方程的求解，有时候我们只需要principal value。例如对于
![alt text](https://heaohan.github.io/files/2016-08-03_141610.jpg)
其解有无数个：
![alt text](https://heaohan.github.io/files/2016-08-03_141716.jpg)
k=0的那一个是principal value：
![alt text](https://heaohan.github.io/files/2016-08-03_142830.jpg)

###Complex argument
复幅角

The principal value of complex number argument measured in radians can be defined as:
- value in the range [0, 2pi]
- values in the range (-pi, pi]

To compute these values one can use functions:
- atan2 with principal value in the range (-π, π]
- atan with principal value in the range (-π/2, π/2]