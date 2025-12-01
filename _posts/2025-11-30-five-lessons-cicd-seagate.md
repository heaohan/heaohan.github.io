---
layout: post
title: "5 Lessons from Implementing CI/CD at Seagate"
subtitle: "What I learned automating deployment for manufacturing software"
date: 2025-11-30
tags: [cicd, devops, software-engineering, manufacturing, lessons-learned]
---

Two years ago, our team's software deployment process looked like this: manual builds, USB drive transfers, crossed fingers, and a lot of hope. Today, we have achieve good progress on our way to push commits that automatically test, build, and deploy to production stations. Here's what I learned making that transition.

## 🎯 The Challenge

Manufacturing software has unique constraints:
- **Hardware dependencies** - Code runs on physical equipment worth millions
- **High reliability requirements** - Downtime costs thousands per hour
- **Multiple stations** - Same codebase, different configurations
- **Legacy code** - Years of accumulated technical debt
- **Risk aversion** - "If it ain't broke, don't fix it" culture

Despite these challenges, our manual process was:
- ❌ Error-prone (wrong version deployed, config mismatches)
- ❌ Slow (hours to deploy a hotfix)
- ❌ Undocumented (tribal knowledge in senior engineers' heads)
- ❌ Fear-inducing (deployments = stress)

Something had to change.

## 📚 Lesson 1: Start Small, Prove Value

**What I wanted to do:** 
Implement full CI/CD for all repositories immediately with automated testing, deployment, and monitoring.

**What I actually did:**
Started with ONE repository and ONE simple pipeline:
```yaml
# First GitHub Actions workflow - just build and test .NET Framework 4.8

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-test:
    runs-on: windows-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Setup NuGet
      uses: NuGet/setup-nuget@v2
      with:
        nuget-version: '6.x'

    - name: Restore NuGet packages
      run: nuget restore **/*.sln

    - name: Setup MSBuild
      uses: microsoft/setup-msbuild@v2

    - name: Build solution
      run: msbuild **/*.sln /p:Configuration=Release /p:Platform="Any CPU"

    - name: Test with VSTest
      uses: darenm/RunVSTests@v1
      with:
        testFiles: |
          **\*test*.dll
          !**\*TestAdapter.dll
          !**\obj\**
```

**Why it worked:**
- Quick wins built credibility
- Low risk allowed experimentation
- Visible benefits encouraged adoption
- Mistakes were cheap to fix

**The result:** After 3 months, other teams were asking "Can we have CI/CD too?"

### Key Takeaway
> Don't boil the ocean. Pick one pain point, solve it well, and let success speak for itself.

## 🧪 Lesson 2: Tests Are Your Safety Net

Early on, I pushed for CI/CD without robust tests. Big mistake.

**What happened:**
- Automated deployments... of broken code
- Fast feedback... that everything was broken
- Quick rollbacks... that we did frequently

**The fix:**
Invested in building a test pyramid:

```
        /\
       /  \      Few: E2E tests with hardware
      /____\
     /      \    Some: Integration tests
    /________\
   /          \  Many: Unit tests
  /____________\
```

**Our testing strategy:**
1. **Unit tests** (NetFramework Test) - Fast, run on every commit

2. **Integration tests** - Test component interactions

3. **Hardware tests** - Staged environment before production
   - Run on dedicated test station
   - Actual cameras and robots
   - Real-world scenarios

### Key Takeaway
> CI/CD without tests is just continuous deployment of bugs. Invest in testing infrastructure first.

## 🏗️ Lesson 3: Infrastructure as Code Is Non-Negotiable

Initially, our build configurations lived in:
- Senior engineer's mind 💭
- Word documents on shared drive 📄
- "How we've always done it" 🤷

**The problem:** Bus factor of 1. If that person left, we were screwed.

**The solution:** Everything in version control.

**Benefits:**
- New team members onboard faster
- Builds reproducible on any machine
- Changes reviewed like code
- History tracked in Git

### Key Takeaway
> If it's not in Git, it doesn't exist. Document your infrastructure like your future self's job depends on it (because it might).

## 🔄 Lesson 4: Gradual Rollout Beats Big Bang

**Blue-Green deployments:**
- Keep old version running
- Deploy new version alongside
- Switch traffic when validated
- Quick rollback if needed

### Key Takeaway
> Move fast, but give yourself undo buttons. Staged rollouts and feature flags are your friends.

## 🤝 Lesson 5: Culture Eats Process for Breakfast

The hardest part wasn't the technical implementation. It was getting people to trust it.

**Resistance I faced:**
- "We've always done it manually, why change?"
- "Automated deployments will break production"
- "I don't trust code I didn't manually verify"
- "This is too risky for our environment"

**How I addressed it:**

**1. Education & Training**
- Brown bag sessions on CI/CD basics
- Hands-on workshops with simple examples
- Documentation with real scenarios

**2. Transparency**
- Made all pipelines visible
- Shared metrics (deployment frequency, failure rate)
- Celebrated wins publicly

**3. Incremental buy-in**
- Let teams opt-in voluntarily
- Supported early adopters heavily
- Showcased their success stories

**4. Address concerns head-on**
- Added manual approval gates for critical deployments
- Kept manual override capability
- Extensive logging and monitoring

**The turning point:** 
When a critical bug hit production at 5 PM on Friday:
- **Old way:** Would've waited until Monday
- **New way:** 
  1. Fix committed at 5:15 PM
  2. Tests passed at 5:20 PM
  3. Deployed to test station at 5:25 PM
  4. Validated and deployed to production at 5:45 PM
  5. Everyone home by 6 PM

After that, resistance melted away.

### Key Takeaway
> Technical solutions are easy. Changing how people work is hard. Invest in people as much as in pipelines.

## 📊 Results After 2 Years

**Metrics that improved:**

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Deployment time | 4+ hours | 15 minutes | **94% faster** |
| Deployment frequency | Weekly | Multiple daily | **20x increase** |
| Failed deployments | ~30% | <5% | **83% reduction** |
| Time to fix bugs | Days | Hours | **~90% faster** |
| Developer satisfaction | 😫 | 😊 | Priceless |

**Unexpected benefits:**
- Better code quality (tests required for merge)
- Faster onboarding (automated setup)
- More experimentation (easy to try and rollback)
- Reduced stress (no more "deployment days")

## 🚀 If I Were Starting Today

Here's what I'd do differently:

1. **Start with tests** - Build testing culture first, CI/CD second
2. **Automate toil** - Identify manual pain points, automate the worst ones
3. **Document everything** - Future you will thank present you
4. **Get stakeholder buy-in early** - Don't surprise people with changes
5. **Measure and communicate** - Track metrics, share wins
6. **Keep it simple** - Don't over-engineer, iterate and improve

## 🎯 Resources That Helped

**Books:**
- *Continuous Delivery* by Jez Humble
- *The DevOps Handbook* by Gene Kim
- *Accelerate* by Nicole Forsgren

**Tools we use:**
- **GitHub Actions** - CI/CD pipelines
- **CMake** - Build system
- **Google Test** - Unit testing
- **Docker** (exploring) - Consistent environments

**Communities:**
- DevOps subreddit
- GitHub Actions community
- Company internal Slack channels

## 💭 Final Thoughts

Implementing CI/CD in a manufacturing environment taught me that:

- **Technical challenges are solvable** - The tools exist and work well
- **Cultural challenges are harder** - But also more rewarding to solve
- **Small wins compound** - Start small, iterate, improve
- **Automation enables innovation** - Less time deploying = more time creating
- **Fear is the mind-killer** - Build safety nets to enable confidence

If you're considering CI/CD for your manufacturing software, I encourage you to start. Pick one small project, build one simple pipeline, and prove it works. The journey is worth it.

## 📫 Questions?

Have questions about CI/CD for manufacturing or hardware-integrated software? Want to share your own experiences? Reach out!

- **Email:** [heaohan@gmail.com](mailto:heaohan@gmail.com)
- **LinkedIn:** [linkedin.com/in/heaohan](https://www.linkedin.com/in/heaohan/)

---

*What's your biggest challenge with software deployment? Let me know - I'd love to hear your perspective!*
