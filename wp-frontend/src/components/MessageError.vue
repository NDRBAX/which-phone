<template v-if="Array.keys(errors).length > 0">
  <div
    v-for="(values, name) in errors"
    :key="name"
    :class="[
      $props.type
        ? 'alert-error alert shadow-lg text-white'
        : 'alert alert-success shadow-lg text-white',
    ]"
  >
    <div class="flex justify-between w-full">
      <div>
        <span v-if="Array.isArray(values)">
          <span v-for="value in values" :key="value">{{ value }}</span>
        </span>
        <span v-else>
          <span class="block sm:inline">{{ values }}</span>
        </span>
      </div>
      <div>
        <svg
          v-on:click="close"
          xmlns="http://www.w3.org/2000/svg"
          class="stroke-current h-6 w-6 hover:-translate-y-0.5 transform transition ease-in-out duration-300 cursor-pointer"
          fill="none"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MessageError",
  props: {
    errors: {
      type: Array,
      default: () => [],
    },
    close: Function,

    type: {
      type: Boolean,
    },
  },
  emits: ["close"],
};
</script>
