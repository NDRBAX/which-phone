<template>
  <div>
    <!-- progress bar for steps -->
    <progress
      class="progress progress-accent w-full px-10 mt-10"
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
              <!-- RADIO -->
              <div
                v-if="data.type === 'radio'"
                class="justify-center space-y-2"
              >
                <div
                  class="text-2xl font-thin font-bold text-gray-700 text-center mb-8"
                >
                  <p>{{ data.label }}</p>
                </div>
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in data.choices"
                    :key="choice.value"
                    class="basis-auto p-3"
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
                      class="flex p-5 text-gray-500 hover:text-gray-700 cursor-pointer peer-checked:text-green-600"
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
                <div
                  class="text-2xl font-thin font-bold text-gray-700 text-center mb-8"
                >
                  <p>{{ data.label }}</p>
                </div>
                <div class="flex flex-wrap flex-row justify-center">
                  <div
                    v-for="choice in data.choices"
                    :key="data.label + choice.value"
                    class="basis-auto p-3"
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
                      class="flex p-5 text-gray-500 hover:text-gray-700 cursor-pointer peer-checked:text-green-600"
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
        class="btn btn-base-300"
        :disabled="currentStepIndex == 1"
        v-on:click="previousStep"
      >
        {{ previous }}
      </button>

      <button id="next" class="btn btn-accent ml-4" v-on:click="nextStep()">
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
          checked: "",
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
            checked: "",
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

label:hover {
  font-weight: 550;
  letter-spacing: 0;
}
/* 
input[type="checkbox"]:checked,
input[type="radio"]:checked {
  font-size: 3.5rem;
} */
</style>
