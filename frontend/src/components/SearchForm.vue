<template>
  <div class="container mx-auto mt-10 max-w-7xl">
    <nav class="mb-20 flex justify-center">
      <ol class="flex">
        <li
          class="relative w-[150px] text-center text-sm font-light italic after:content-[''] after:absolute after:left-[50%] after:top-[200%] after:w-5 after:h-5 after:bg-indigo-500 after:rounded-full after:z-50"
        >
          Step 1
        </li>
        <li
          class="relative w-[150px] text-center text-sm font-light italic before:content-[''] before:absolute before:left-[-50%] before:top-[calc(200%+0.5rem)] before:w-full before:h-1 after:bg-gray-300 before:bg-gray-300 after:content-[''] after:absolute after:left-[50%] after:top-[200%] after:w-5 after:h-5 after:rounded-full after:z-50"
          :class="{ stepFull: step >= 1 }"
        >
          Step 2
        </li>

        <li
          class="relative w-[150px] text-center text-sm font-light italic before:content-[''] before:absolute before:left-[-50%] before:top-[calc(200%+0.5rem)] before:w-full before:h-1 before:bg-gray-300 after:content-[''] after:absolute after:left-[50%] after:top-[200%] after:w-5 after:h-5 after:bg-gray-300 after:rounded-full after:z-50"
          :class="{ stepFull: step >= 2 }"
        >
          Step 3
        </li>
      </ol>
    </nav>

    <component v-bind:is="steps[step]" v-bind:formValues="values"></component>
    <div class="flex items-center justify-between mt-5" v-if="step < 3">
      <button class="btn btn-accent" v-on:click="previousStep" v-if="step > 0">
        Previous
      </button>
      <button class="btn btn-accent" v-on:click="nextStep">Next</button>
    </div>
  </div>
</template>

<script>
import FirstStep from "./steps/FirstStep.vue";
import SecondStep from "./steps/SecondStep.vue";
import ThirdStep from "./steps/ThirdStep.vue";
import FinalStep from "./steps/FinalStep.vue";
import { ref } from "vue";
import { useFormStore } from "../stores/formValues";

export default {
  setup() {
    const step = ref(0);

    const values = useFormStore();

    const steps = [FirstStep, SecondStep, ThirdStep, FinalStep];

    const nextStep = () => {
      if (step.value < steps.length - 1) {
        step.value++;
      }
    };

    const previousStep = () => {
      if (step.value > 0) {
        step.value--;
      }
    };
    return { step, steps, nextStep, previousStep, values };
  },
};
</script>
