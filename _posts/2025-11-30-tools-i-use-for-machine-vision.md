---
layout: post
title: "My Machine Vision Development Setup"
subtitle: "Tools and workflows for building production vision systems"
date: 2025-11-30
tags: [machine-vision, tools, productivity, software-engineering]
---

After years of building machine vision systems for manufacturing, I've settled on a set of tools and workflows that maximize productivity. Here's what's in my toolkit and why.

## 🎯 Vision Libraries & Frameworks

### Halcon (Primary)
**When I use it:** Production vision systems requiring robustness and speed

**Why I love it:**
- Extremely fast and reliable operators
- Excellent calibration and 3D tools
- Great documentation with example code
- HDevelop IDE is perfect for rapid prototyping

**Trade-offs:**
- Expensive licensing (but worth it for production)
- Proprietary ecosystem
- Learning curve for beginners

**Typical use case:** Vision-guided robotics, high-precision measurement, geometric analysis

### Halcon
**When I use it:** Deep learning integration and complex inspection tasks

**Why it's useful:**
- HDevelop makes DL deployment straightforward
- Good integration with cameras and hardware
- Powerful for defect detection
- Industry-standard reliability

**Trade-offs:**
- Also expensive
- Less flexible than open-source alternatives
- Vendor lock-in

**Typical use case:** Defect detection, anomaly detection, complex pattern matching

### OpenCV (Python/C++)
**When I use it:** Prototyping, research, custom algorithms

**Why I still use it:**
- Free and open-source
- Massive community and resources
- Complete control over implementation
- Great for learning and experimentation

**Trade-offs:**
- More coding required vs commercial tools
- Performance optimization needed for production
- Less out-of-the-box features

**Typical use case:** Algorithm development, proof-of-concepts, custom processing

## 💻 Development Environment

### IDEs
- **Visual Studio 2022** - Primary C++ development for production systems
- **VS Code** - Python, configuration files, quick edits
- **HDevelop** - Halcon algorithm development and prototyping

### Version Control
- **Git + GitHub** - All code versioned, even small scripts
- **GitHub Actions** - CI/CD pipelines for automated testing and deployment

### Testing Frameworks
- **C# NetFramework Unit Test** - Unit testing for vision algorithms
- **pytest (Python)** - Testing data processing and utilities
- **Manual test sequences** - Hardware-in-the-loop validation

## 🔧 Supporting Tools

### Image Annotation & Dataset Management
- **LabelImg** - Quick bounding box annotations
- **CVAT** - More complex annotation tasks
- **Custom Python scripts** - Data augmentation and preprocessing

### Performance Profiling
- **Visual Studio Profiler** - Finding bottlenecks in C++ code
- **CUDA Profiler** - GPU performance analysis
- **Python cProfile** - Python optimization

### Communication
- **Microsoft Teams** - Daily team communication
- **Email** - Formal communications and documentation
- **In-person reviews** - Critical for hardware-integrated systems

## 🎨 My Typical Workflow

### 1. Prototype in HDevelop/Python
Start with quick experiments to validate approach:
```python
# Quick prototype in Python
import cv2
import numpy as np

# Test algorithm with sample images
img = cv2.imread('test_image.png')
# ... rapid iteration ...
```

### 2. Validate with Real Data
Test on actual production images:
- Edge cases
- Lighting variations
- Part variations
- Different camera positions

### 3. Implement in Production Language (C##)
Once algorithm is proven

### 4. Create Automated Tests
Cover critical functionality

### 5. Deploy via CI/CD
- Automated builds on commit
- Unit tests must pass
- Integration tests on test station
- Staged rollout to production

## 📊 Data Management Strategy

### Image Storage
- **Local SSD** - Active development images
- **Network share** - Shared datasets and archives
- **Cloud backup** - Critical datasets

### Dataset Organization
```
datasets/
├── raw/              # Original unprocessed images
├── annotated/        # Labeled data
├── train/            # Training sets
├── validation/       # Validation sets
└── test/             # Test sets
```

### Version Control for Data
- **DVC (Data Version Control)** - For large datasets
- **Git LFS** - For smaller image sets
- **Metadata in Git** - Dataset descriptions and split info

## 🎓 Learning Resources I Actually Use

### Documentation
- Official Halcon reference manual (seriously, read it)
- Stack Overflow (of course)

### Books
- *Machine Vision Handbook* - Industry perspective

### Communities
- Company internal channels - Domain knowledge

## 💡 Lessons Learned

1. **Start simple** - Get basic version working first, then optimize
2. **Test on real data early** - Synthetic data lies
3. **Version everything** - Code, configs, even test images
4. **Automate testing** - Manual testing doesn't scale
5. **Document assumptions** - Future you will forget why
6. **Profile before optimizing** - Measure, don't guess
7. **Backup critical data** - Lost datasets = lost time

## 🔮 Tools I'm Exploring

- **ONNX Runtime** - Model deployment standardization
- **DVC** - Better data version control

## 📫 What's Your Setup?

I'm always curious about what tools other vision engineers use. If you have suggestions or use different tools, I'd love to hear about them!

**What tools do you rely on for machine vision development?** Feel free to reach out via [email](mailto:heaohan@gmail.com) or [LinkedIn](https://www.linkedin.com/in/heaohan/)!

---

*This post reflects my personal experiences and opinions. Tool choices should be based on your specific requirements, budget, and constraints.*
