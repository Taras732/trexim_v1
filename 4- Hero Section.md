# Hero Section Technical Spec

**Role:** First impression. Premium, technological, "The Future".

## Visual Reference
Based on provided image (Gifo.ai style):
- **Background:** Soft gradient (Dark Navy #0B1120 to slightly lighter blue/purple accents).
- **Layout:** Centered alignment.
- **Typography:**
  - H1: Benzin Regular. Large, bold, commanding.
  - Subtext: Futura. Clean, readable opacity 80%.
- **Elements:**
  1. **"Trusted by" Pill:** Glassmorphism effect at the top.
  2. **Main Headline:** "Operating System for Global Logistics" (or similar).
  3. **Subheadline:** "Automate 70% of routine. AI-driven transparency. Digital integrity."
  4. **CTA Area:** Input field + "Get Early Access" button (Gradient button).
  5. **Visual Anchor:** A "floating" dashboard mock-up at the bottom of the viewport, fading in/sliding up.

## Technical Implementation

### HTML Structure
```html
<section class="relative overflow-hidden bg-dark-navy min-h-screen flex flex-col items-center justify-center pt-24">
    <!-- Background Gradients/Blobs -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[500px] bg-gradient-to-b from-accent-blue/20 to-transparent blur-3xl"></div>

    <!-- Trusted By Pill -->
    <div class="glass-pill mb-8 animate-fade-in-down">
        <span>Trusted by Industry Leaders</span>
    </div>

    <!-- Typography -->
    <div class="text-center z-10 max-w-4xl px-4">
        <h1 class="font-benzin text-5xl md:text-7xl text-white mb-6 leading-tight">
             The <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500">Neural Connect</span> <br /> 
             for Logistics
        </h1>
        <p class="font-futura text-gray-300 text-lg md:text-xl mb-10 max-w-2xl mx-auto">
            Unite shippers, carriers, and banks in one trusted digital ecosystem.
        </p>
    </div>

    <!-- CTA -->
    <div class="flex flex-col sm:flex-row gap-4 w-full max-w-md z-10 mb-20">
        <input type="email" placeholder="Business Email" class="input-glass flex-1" />
        <button class="btn-primary">Request Access</button>
    </div>

    <!-- Visual Anchor (Dashboard Mockup) -->
    <div class="relative w-full max-w-6xl -mb-32 z-10 animate-slide-up">
        <div class="glass-panel rounded-t-3xl border-t border-white/10 p-4 shadow-2xl bg-dark-navy/80 backdrop-blur-xl">
             <!-- Placeholder for Dashboard Image/UI -->
             <div class="h-[400px] bg-white/5 rounded-xl border border-white/5 flex items-center justify-center">
                <span class="text-white/30 font-benzin">Mission Control Interface</span>
             </div>
        </div>
    </div>
</section>
```

### Tailwind Custom Config
- `colors`:
  - `dark-navy`: `#020617` (Slate 950) or custom hex.
  - `accent-blue`: `#3b82f6`
- `fontFamily`:
  - `benzin`: ['Benzin', 'sans-serif']
  - `futura`: ['Futura', 'sans-serif']

### Animations
- Simple CSS animations for `fade-in-down` and `slide-up`.

