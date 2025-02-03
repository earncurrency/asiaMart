<template>
    <div id="animation-carousel" class="relative w-full lg:top-16" data-carousel="static">
        <!-- Carousel wrapper -->
        <div class="relative h-56 overflow-hidden md:h-[410px]">
            <!-- Transition wrapper -->
            <transition name="carousel-transition" @before-enter="beforeEnter" @enter="enter" @leave="leave">
                <!-- Item display conditionally based on the currentSlide -->
                <div :key="currentSlide" class="duration-200 ease-linear" data-carousel-item>
                    <img :src="images[currentSlide]"
                        class="absolute block w-full -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2 object-cover"
                        alt="...">
                </div>
            </transition>
        </div>
        <!-- Slider controls -->
        <button type="button"
            class="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
            @click="previousSlide">
            <span
                class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M5 1 1 5l4 4" />
                </svg>
                <span class="sr-only">Previous</span>
            </span>
        </button>
        <button type="button"
            class="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
            @click="nextSlide">
            <span
                class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 dark:bg-gray-800/30 group-hover:bg-white/50 dark:group-hover:bg-gray-800/60 group-focus:ring-4 group-focus:ring-white dark:group-focus:ring-gray-800/70 group-focus:outline-none">
                <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 9 4-4-4-4" />
                </svg>
                <span class="sr-only">Next</span>
            </span>
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentSlide: 0,
            images: [
                'https://images.deliveryhero.io/image/fd-th/LH/ws9f-listing.jpg',
                'https://images.deliveryhero.io/image/fd-th/LH/e4gw-listing.jpg',
                'https://shopee.co.th/blog/wp-content/uploads/2020/10/%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%A1%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%81%E0%B9%88.jpg',
                'https://img-global.cpcdn.com/recipes/8d36694f728a8620/1200x630cq70/photo.jpg'
            ],
            cycleInterval: null
        };
    },
    methods: {
        nextSlide() {
            this.currentSlide = this.currentSlide + 1;
            if (this.currentSlide == this.images.length) {
                this.currentSlide = 0;
            }
            this.resetAutoCycle();
        },
        previousSlide() {
            this.currentSlide = this.currentSlide - 1;
            if (this.currentSlide < 0) {
                this.currentSlide = this.images.length - 1;;
            }
            this.resetAutoCycle();
        },
        autoCycle() {
            if (this.cycleInterval === null) {
                this.cycleInterval = setInterval(this.nextSlide, 5000);
            }
        },
        resetAutoCycle() {
            // หยุดการหมุนอัตโนมัติที่กำลังทำงานอยู่
            if (this.cycleInterval !== null) {
                clearInterval(this.cycleInterval);
            }
            // เริ่มการหมุนอัตโนมัติใหม่
            this.cycleInterval = setInterval(this.nextSlide, 5000);
        },

        beforeEnter(element) {
            element.style.opacity = 0;
        },
        enter(element, done) {
            // Set the transition to fade-in
            element.offsetHeight; // trigger reflow to apply styles correctly
            element.style.transition = 'opacity 1s ease';
            element.style.opacity = 1;
            done();
        },
        leave(element, done) {
            // Set the transition to fade-out
            element.style.transition = 'opacity 1s ease';
            element.style.opacity = 0;
            done();
        }
    },
    mounted() {
        this.autoCycle();
    },

};
</script>
