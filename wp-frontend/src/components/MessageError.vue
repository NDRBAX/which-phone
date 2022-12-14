<template>
  <div
    class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mt-5"
    role="alert"
    v-if="Object.keys(errors).length > 0"
  >
    <div v-for="(values, name) in errors" :key="name">
      <!-- <strong class="font-bold">Error: {{ name }}!</strong> -->
      <span v-if="Array.isArray(values)">
        <span v-for="value in values" :key="value" class="block sm:inline"
          ><li>{{ value }}</li></span
        >
      </span>
      <span v-else>
        <span class="block sm:inline">{{ values }}</span>
      </span>

      <span class="absolute top-0 bottom-0 right-0 px-4 py-3">
        <svg
          v-on:click="$emit('close')"
          class="fill-current h-6 w-6 text-red-500"
          role="button"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <title>Close</title>
          <path
            d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"
          />
        </svg>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "MessageError",
  props: {
    errors: {},
  },
};
</script>
