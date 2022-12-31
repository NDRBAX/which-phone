<template>
  <div
    class="animated-number xs:text-xl sm:text-2xl md:text-4xl font-bold text-teal-accent-400"
  >
    {{ formattedValue }}
  </div>
</template>

<script>
export default {
  name: "AnimatedNumber",
  props: {
    value: {
      type: Number,
      required: true,
    },
    duration: {
      type: Number,
      default: 2000,
    },
  },
  data() {
    return {
      currentValue: 0,
    };
  },
  mounted() {
    this.animateNumber();
  },
  computed: {
    formattedValue() {
      return this.currentValue.toLocaleString();
    },
  },
  methods: {
    animateNumber() {
      const start = performance.now();
      const end = start + this.duration;

      const step = (timestamp) => {
        let progress = timestamp - start;
        this.currentValue = Math.min(
          Math.floor((progress / this.duration) * this.value),
          this.value
        );

        if (timestamp < end) {
          window.requestAnimationFrame(step);
        }
      };

      window.requestAnimationFrame(step);
    },
  },
};
</script>
