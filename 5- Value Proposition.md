# Value Proposition Technical Spec

**Role:** Rational conversion. Explain *why* Trexim is better via concrete benefits.

## Visual Reference
- **Style:** LottieLab Bento Grid (Bold, vivid cards).
- **Theme:** Deep dark background + Vibrant Accents.
- **Card Styles:**
    1.  **Dark Card (Left):** Minimalist, dark gray/black with subtle UI glow.
    2.  **Purple Gradient Card (Center):** Vivid purple/violet gradient background. Promoting "Interactive/Trust".
    3.  **Teal Card (Right Bottom):** Bright teal/green block. High contrast for "Speed/Standard".
    4.  **Dark Card (Right Top):** Utility style.


## Content Structure

### 1. Efficiency Card (Large/Featured)
- **Anchor:** "70%" (Big Text)
- **Title:** Auotmation
- **Text:** "Forget routine. AI handles operational tasks, freeing your team for strategic growth."
- **Visual:** Abstract AI brain/network or progress bar animation.

### 2. Trust Card
- **Anchor:** "KEP / Digital Sign" Icon or "100%"
- **Title:** Digital Integrity
- **Text:** "Zero space for manipulation. Every deal signed with KEP. 24/7 Legal transparency."
- **Visual:** Shield/Lock icon with glow.

### 3. Speed Card
- **Anchor:** "0s" or Lightning Icon
- **Title:** Instant Sync
- **Text:** "Unified environment for banks, carriers, and shippers. Payments move faster than cargo."
- **Visual:** Pulse/Data stream effect.

## Technical Implementation

### HTML Structure (Grid)
```html
<section class="relative bg-dark-navy py-24 px-4 overflow-hidden">
    <!-- Section Header -->
    <div class="max-w-7xl mx-auto mb-16 text-center">
        <h2 class="text-3xl md:text-5xl font-bold text-white mb-6">Old Logistics vs <span class="text-blue-500">Trexim World</span></h2>
    </div>

    <!-- Bento Grid -->
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Card 1: Automation (Wide - spans 2 cols on LG if needed, or just 1 large) -->
        <div class="group relative rounded-3xl bg-white/5 border border-white/10 p-8 hover:bg-white/10 transition-all duration-500 overflow-hidden lg:col-span-1 lg:row-span-2">
            <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-blue-500/20 rounded-full blur-[80px]"></div>
            <div class="relative z-10 h-full flex flex-col justify-between">
                <div>
                    <h3 class="text-7xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400 mb-4">70%</h3>
                    <h4 class="text-2xl font-bold text-white mb-4">Automation</h4>
                    <p class="text-gray-400 leading-relaxed">Forget routine. AI handles operational tasks, freeing your team for strategic growth.</p>
                </div>
                <!-- Visual Decoration -->
                <div class="mt-8 rounded-2xl bg-[#0B1120] border border-white/5 p-4 mx-4 translate-y-4 group-hover:translate-y-2 transition-transform">
                     <!-- Fake AI Processing UI -->
                     <div class="flex items-center gap-3 mb-3">
                        <div class="w-2 h-2 rounded-full bg-blue-500 animate-ping"></div>
                        <div class="h-1.5 w-24 bg-blue-500/30 rounded-full overflow-hidden">
                            <div class="h-full bg-blue-500 w-2/3"></div>
                        </div>
                     </div>
                     <div class="space-y-2">
                        <div class="h-2 w-full bg-white/5 rounded"></div>
                        <div class="h-2 w-3/4 bg-white/5 rounded"></div>
                     </div>
                </div>
            </div>
        </div>

        <!-- Card 2: Trust -->
        <div class="group relative rounded-3xl bg-white/5 border border-white/10 p-8 hover:bg-white/10 transition-all duration-500 overflow-hidden">
             <div class="absolute bottom-0 left-0 -ml-10 -mb-10 w-40 h-40 bg-purple-500/20 rounded-full blur-[60px]"></div>
             <div class="relative z-10">
                <div class="w-12 h-12 rounded-xl bg-purple-500/20 flex items-center justify-center text-purple-400 mb-6">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                </div>
                <h4 class="text-xl font-bold text-white mb-2">Digital Integrity</h4>
                <p class="text-sm text-gray-400 mb-4">Zero space for manipulation.</p>
                <div class="p-3 rounded-lg bg-black/20 border border-white/5 flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-green-500/10 flex items-center justify-center text-green-400 text-xs">KEP</div>
                    <div class="text-xs text-gray-300">Signed & Verified</div>
                </div>
             </div>
        </div>

        <!-- Card 3: Speed -->
        <div class="group relative rounded-3xl bg-white/5 border border-white/10 p-8 hover:bg-white/10 transition-all duration-500 overflow-hidden">
            <div class="absolute top-0 right-0 w-full h-full bg-gradient-to-br from-transparent to-blue-500/5 group-hover:to-blue-500/10 transition-colors"></div>
            <div class="relative z-10">
                 <div class="text-4xl text-yellow-400 mb-4">⚡</div>
                 <h4 class="text-xl font-bold text-white mb-2">Instant Sync</h4>
                 <p class="text-sm text-gray-400">Unified environment. Payments move faster than cargo.</p>
            </div>
        </div>

    </div>
</section>
```
