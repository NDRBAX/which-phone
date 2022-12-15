<template>
  <div>
    <!-- progress bar for steps -->
    <progress
      class="progress progress-success w-full px-10 mt-10"
      max="100"
      :value="progressValue(currentStepIndex)"
    ></progress>
    <MessageError :errors="errors" @close="closeMessageError" class="m-10" />
    <div class="flex flex-col items-center justify-center">
      <div
        class="card p-[50px] mt-5 w-full max-w-4xl bg-white rounded shadow-xl"
      >
        <div class="card-body">
          <form class="space-y-3">
            <div v-for="data in currentStep.questions" :key="data.label">
              <div class="text-4xl font-bold text-gray-900 text-center mb-8">
                <p
                  class="inline-block px-3 py-px mb-4 text-xs font-semibold tracking-wider text-teal-900 uppercase rounded-full bg-teal-accent-400"
                >
                  {{ data.step }}
                </p>
                <p v-html="data.label"></p>
              </div>
              <!-- RADIO -->
              <div
                v-if="data.type === 'radio'"
                class="justify-center space-y-2"
              >
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in data.choices"
                    :key="choice.value"
                    class="basis-auto px-3 py-1"
                  >
                    <input
                      class="sr-only peer"
                      type="radio"
                      :value="choice.label"
                      :id="choice.value"
                      v-model="formData[currentIndex].checked"
                    />
                    <label
                      :for="choice.value"
                      class="flex uppercase duration-300 font-semibold transform text-white text-4xl hover:text-teal-accent-400 font-black cursor-pointer peer-checked:text-teal-accent-400"
                    >
                      {{ choice.label }}
                    </label>
                  </div>
                </div>
              </div>
              <!-- CHECKBOX -->
              <div
                v-else-if="data.type === 'checkbox'"
                class="justify-center space-y-2"
              >
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in data.choices"
                    :key="data.label + choice.value"
                    class="basis-auto px-3"
                  >
                    <input
                      class="sr-only peer"
                      type="checkbox"
                      :value="choice.label"
                      :id="choice.value"
                      v-model="formData[currentIndex].checked"
                    />
                    <label
                      :for="choice.value"
                      class="flex uppercase duration-300 font-semibold transform text-white text-4xl hover:text-teal-accent-400 font-black cursor-pointer peer-checked:text-teal-accent-400"
                    >
                      {{ choice.label }}
                    </label>
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
        id="previous"
        class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-gray-900 bg-white ring-inset ring-2 ring-gray-900 enabled:hover:ring-0 enabled:hover:bg-gray-900 enabled:hover:text-white transition duration-200 rounded shadow-md md:w-auto focus:shadow-outline focus:outline-none disabled:opacity-50"
        :disabled="currentStepIndex == 1"
        v-on:click="previousStep"
      >
        {{ previous }}
      </button>

      <button
        id="next"
        class="inline-flex items-center justify-center w-full h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md md:w-auto bg-teal-accent-400 enabled:hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none ml-4 disabled:opacity-50"
        v-on:click="nextStep()"
      >
        {{ next }}
      </button>
    </div>
  </div>
</template>
<script>
import { useCheckedStore } from "../stores/checked";

import MessageError from "./MessageError.vue";
export default {
  name: "MultiStepForm",
  components: {
    MessageError,
  },
  data() {
    return {
      formData: [
        {
          step: 1,
          checked: "",
        },
        {
          step: 2,
          checked: [],
        },
        {
          step: 3,
          checked: [],
        },
        {
          step: 4,
          checked: [],
        },
        {
          step: 5,
          checked: "",
        },
      ],
      errors: [],
      currentIndex: 0,
      currentStep: this.steps[0],
      currentStepIndex: this.steps.findIndex((step) => step.active) + 1,
      previous: "Previous",
      next: "Next",
      store: useCheckedStore(),
      maxChecked: 3,
    };
  },
  props: {
    steps: {
      title: String,
      active: Boolean,
      question: [
        {
          label: String,
          type: String,
          choices: [{ value: String, label: String }],
        },
      ],
    },
  },
  computed: {
    checkboxMaxChecked() {
      return this.formData[this.currentIndex].checked.length <= this.maxChecked;
    },
  },
  methods: {
    progressValue(index) {
      return (100 / this.steps.length) * index;
    },
    nextStep() {
      if (this.formData[this.currentIndex].checked.length === 0) {
        this.errors = ["Please select at least one option"];
        console.log(this.errors);
      } else if (this.next === "Submit") {
        this.store.setCheckedByStep(
          this.formData[this.currentIndex].step,
          this.formData[this.currentIndex].checked
        );
        console.log("submit");
        if (this.compareData(this.formData, this.store.getAllValues)) {
          this.store.submit();
        } else {
          this.errors = ["Something went wrong. Please try again."];
        }
        this.previous = "Search again";
        document.getElementById("next").disabled = true;
      } else {
        this.store.setCheckedByStep(
          this.formData[this.currentIndex].step,
          this.formData[this.currentIndex].checked
        );
        this.currentStepIndex++;
        this.currentIndex++;
        this.currentStep = this.steps[this.currentStepIndex - 1];
        this.closeMessageError();
      }
    },
    previousStep() {
      if (
        this.previous === "Search again" &&
        this.currentStepIndex === this.steps.length
      ) {
        this.store.clearStore();
        this.currentStepIndex = 1;
        this.currentStep = this.steps[this.currentStepIndex - 1];
        this.currentIndex = 0;
        // reset formData
        this.formData = [
          {
            step: 1,
            checked: "",
          },
          {
            step: 2,
            checked: [],
          },
          {
            step: 3,
            checked: [],
          },
          {
            step: 4,
            checked: [],
          },
          {
            step: 5,
            checked: "",
          },
        ];
      } else if (this.currentStepIndex > 1) {
        this.currentStepIndex--;
        this.currentStep = this.steps[this.currentStepIndex - 1];
        this.currentIndex--;
      }
    },
    compareData(local, store) {
      let localData = [];
      let storeData = [];

      local.forEach((data) => {
        if (typeof data.checked === "object") {
          data.checked.forEach((choice) => {
            localData.push(choice);
          });
        } else {
          localData.push(data.checked);
        }
      });

      store.forEach((data) => {
        if (typeof data === "object") {
          data.checked.forEach((choice) => {
            if (choice.length <= 3) {
              choice.forEach((value) => {
                storeData.push(value);
              });
            } else {
              storeData.push(choice);
            }
          });
        } else {
          storeData.push(data);
        }
      });

      let compare = localData.every(
        (value, index) => value === storeData[index]
      );

      return compare;
    },

    closeMessageError() {
      this.errors = [];
    },
  },
  watch: {
    currentStepIndex() {
      this.steps.forEach((step) => (step.active = false));
      this.currentStep.active = true;

      if (this.currentStepIndex === this.steps.length) {
        this.next = "Submit";
        this.previous = "Previous";
      } else if (this.currentStepIndex === 1) {
        document.getElementById("next").disabled = false;

        this.previous = "Previous";
        this.next = "Next";
      } else {
        this.previous = "Previous";
        this.next = "Next";
      }
    },
    checkboxMaxChecked() {
      if (this.currentStep.questions[0].type === "checkbox") {
        if (this.formData[this.currentIndex].checked.length > this.maxChecked) {
          this.errors = [`Please select at most ${this.maxChecked} options`];
          console.log(this.errors);
          // remove first element of array
          this.formData[this.currentIndex].checked.shift();
          console.log(this.formData[this.currentIndex].checked);
        } else {
          this.errors = [];
        }
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Train+One&display=swap");

label {
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #1de9b6;
}

label:hover {
  -webkit-text-stroke-width: 0px;
}

input:checked + label {
  -webkit-text-stroke-width: 0px;
}
/* 
button:disabled,
button:disabled:hover {
  background-color: gray;
  color: #fff;
  border: 1px solid #1de9b6;
} */
</style>
