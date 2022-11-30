<template>
  <div>
    <!-- progress bar for steps -->
    <progress
      class="progress progress-accent w-full px-10 mt-10"
      max="100"
      :value="progressValue(currentStepIndex)"
    ></progress>

    <!-- multistep form card -->
    <div class="flex flex-col items-center justify-center">
      <div class="card p-3 mt-5 w-full max-w-2xl bg-white rounded shadow-xl">
        <div class="card-body">
          <form class="space-y-3">
            <div v-for="question in currentStep.questions" :key="question.id">
              <!-- IF QUESTION IS CHECKBOX -->
              <div
                v-if="question.type === 'checkbox'"
                class="justify-center space-y-2"
              >
                <div
                  class="text-2xl font-thin font-bold text-gray-700 text-center mb-8"
                >
                  {{ question.label }}
                </div>
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in question.choices"
                    :key="choice.id"
                    class="basis-auto p-3"
                  >
                    <input
                      class="sr-only peer"
                      type="checkbox"
                      :value="choice.title"
                      :name="choice.title"
                      :id="choice.title"
                      v-model="choice.id"
                      v-on:change="handleCheckboxChange(choice.title)"
                    />
                    <label
                      class="flex p-5 text-gray-500 hover:text-gray-700 cursor-pointer peer-checked:text-green-600"
                      :for="choice.title"
                      >{{ choice.title }}</label
                    >
                  </div>
                </div>
              </div>

              <!-- IF QUESTION IS RADIO -->
              <div v-else-if="question.type === 'radio'" class="flex flex-col">
                <div
                  class="text-2xl font-thin font-bold text-gray-700 text-center mb-8"
                >
                  {{ question.label }}
                </div>
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in question.choices"
                    :key="choice.id"
                    class="basis-auto p-3"
                  >
                    <input
                      class="sr-only peer"
                      type="radio"
                      :value="choice.title"
                      :name="choice.title"
                      :id="choice.title"
                      v-model="question.title"
                      v-on:change="handleRadioChange"
                    />
                    <label
                      class="flex p-5 text-gray-500 hover:text-gray-700 cursor-pointer peer-checked:text-green-600"
                      :for="choice.title"
                      >{{ choice.title }}</label
                    >
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- previous and next button -->
    <div class="flex flex-row items-center justify-center mt-10">
      <button
        class="btn btn-base-300"
        v-on:click="previousStep"
        :disabled="currentStepIndex == 1"
      >
        Previous
      </button>
      <button class="btn btn-accent ml-4" v-on:click="nextStep">
        {{ next }}
      </button>
    </div>
  </div>
</template>

<script>
import { ref, inject, watchEffect } from "vue";
import { useCheckedStore } from "../store/checked";

export default {
  name: "SearchView",
  setup() {
    const steps = inject("dataENG").formData;
    const currentStep = ref(steps[0]); // current step
    const currentStepIndex = ref(steps.findIndex((step) => step.active) + 1); // current step index
    let next = ref("Next");

    // when current step is last step, next button to submit
    watchEffect(() => {
      if (currentStepIndex.value === steps.length) {
        next.value = "Submit";
      } else {
        next.value = "Next";
      }
    });

    // send total number of step to store
    const { setTotalSteps } = useCheckedStore();
    setTotalSteps(steps.length);

    // Progress bar
    function progressValue(step) {
      return step * (100 / steps.length);
    }

    const nextStep = () => {
      if (currentStepIndex.value < steps.length) {
        currentStepIndex.value++;
        currentStep.value = steps[currentStepIndex.value - 1];
      }
    };

    // handdleRadioChange function to send data to store
    const { setChecked } = useCheckedStore();
    function handleRadioChange() {
      setChecked(currentStep.value);
      const { getChecked } = useCheckedStore();
      if (currentStepIndex.value < steps.length) {
        currentStepIndex.value++;
        currentStep.value = steps[currentStepIndex.value - 1];
      } else {
        console.log(getChecked());
      }
    }

    const maxChecked = ref(3);
    let checkedStorage = [];

    // handdleCheckboxChange function to send data to store
    function handleCheckboxChange(item) {
      currentStep.value.questions[0].choices.forEach((choice) => {
        if (choice.title === item) {
          if (checkedStorage.length < maxChecked.value) {
            if (choice.id) {
              checkedStorage.push(item);
            } else {
              checkedStorage = checkedStorage.filter((i) => i !== item);
            }
          } else {
            if (choice.id) {
              choice.id = false;
            } else {
              checkedStorage = checkedStorage.filter((i) => i !== item);
            }
          }
        }
      });

      console.log(checkedStorage);
    }
    // previous step
    const previousStep = () => {
      if (currentStepIndex.value > 1) {
        currentStepIndex.value--;
        currentStep.value = steps[currentStepIndex.value - 1];
      }
    };

    // submit form

    return {
      steps,
      currentStep,
      currentStepIndex,
      progressValue,
      nextStep,
      previousStep,
      next,
      handleRadioChange,
      handleCheckboxChange,
    };
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Train+One&display=swap");

label {
  display: inline;
  position: relative;

  /*label styling*/
  border: 0px solid #000;
  font-family: "Train One", cursive;
  font-size: 1.7rem;
  font-weight: 500;
  line-height: 14px;
  vertical-align: baseline;
  white-space: nowrap;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  padding: 0;
}

input[type="checkbox"]:checked,
input[type="radio"]:checked {
  font-size: 3.5rem;
}
</style>
