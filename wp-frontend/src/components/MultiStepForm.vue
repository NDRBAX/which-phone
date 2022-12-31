<template>
  <CustomLoader v-if="loading" />
  <div class="xs:text-lg sm:text-2xl md:text-3xl lg:text-4xl text-4xl">
    <div class="w-2/3 mx-auto text-lg flex justify-center">
      <MessageError
        :errors="errors"
        :close="closeMessageError"
        :type="isError"
      />
    </div>
    <div class="flex justify-center text-white xs:grid xs:grid-cols-10 w-full">
      <div
        class="text-lg xs:text-xs sm:text-sm sm-mx-auto xs:col-start-1 xs:col-span-4 sm:col-start-2 sm:col-span-8 mx-auto md:col-start-1 md:col-span-10 lg:col-start-2 lg:col-span-8"
      >
        <ul
          class="steps steps-vertical xs:overflow-hidden sm:overflow-auto sm:steps-horizontal md:w-full xs:px-2 md:px-10 lg:px-0 sm:mt-10"
        >
          <li
            v-for="step in $props.steps"
            :key="step.index"
            :class="
              'step ' +
              (currentStepIndex === step.index
                ? 'step-success'
                : isStepCompleted(step.index)
                ? 'step-success'
                : '')
            "
          >
            <span
              :class="
                currentStepIndex === step.index
                  ? 'px-3  py-px text-xs sm:text-[0.7rem] md:text-xs xs:text-[0.6rem] font-semibold tracking-wider text-white uppercase rounded-full bg-teal-accent-400'
                  : 'px-3 py-px text-xs sm:text-[0.7rem] md:text-xs xs:text-[0.6rem] font-semibold tracking-wider text-white mt-2 text-teal-900 uppercase rounded-full'
              "
              >{{ step.questions[0].step }}</span
            >
          </li>
        </ul>
      </div>

      <div
        class="flex flex-col xs:px-2 items-center justify-center xs:col-start-5 xs:col-span-6 sm:col-span-10"
      >
        <div class="card lg:p-[25px] w-full max-w-4xl bg-transparent">
          <div class="card-body">
            <form class="space-y-3">
              <div v-for="data in currentStep.questions" :key="data.label">
                <div class="font-bold text-gray-900 text-center mb-8">
                  <p v-html="data.label"></p>
                </div>
                <!-- RADIO -->
                <div
                  v-if="data.type === 'radio'"
                  class="justify-center text-center space-y-2 xs:text-sm sm:text-2xl md:text-3xl lg:text-4xl text-4xl"
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
                        v-model="formData[currentStepIndex].checked"
                      />
                      <label
                        :for="choice.value"
                        class="flex uppercase duration-300 font-semibold transform text-white hover:text-teal-accent-400 font-black cursor-pointer peer-checked:text-teal-accent-400 :disabled-opacity-50"
                      >
                        {{ choice.label }}
                      </label>
                    </div>
                  </div>
                </div>
                <!-- CHECKBOX -->
                <div
                  v-else-if="data.type === 'checkbox'"
                  class="justify-center space-y-2 xs:text-sm sm:text-2xl md:text-3xl lg:text-4xl text-4xl text-center"
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
                        v-model="formData[currentStepIndex].checked"
                      />
                      <label
                        :for="choice.value"
                        class="flex uppercase duration-300 font-semibold transform text-white hover:text-teal-accent-400 font-black cursor-pointer peer-checked:text-teal-accent-400 :disabled-opacity-50"
                      >
                        {{ choice.label }}
                      </label>
                    </div>
                  </div>
                </div>
              </div>
            </form>
            <!-- previous and next button -->
            <div
              class="flex flex-row items-center justify-center xs:mt-5 sm:mt-10 mb-20 text-lg"
            >
              <button
                id="previous"
                class="inline-flex items-center justify-center xs:w-20 xs:text-sm sm md sm:w-44 sm:h-12 xs:h-10 px-6 font-medium tracking-wide text-gray-900 bg-white ring-inset ring-2 ring-gray-900 enabled:hover:ring-0 enabled:hover:bg-gray-900 enabled:hover:text-white transition duration-200 rounded shadow-md focus:shadow-outline focus:outline-none disabled:opacity-50"
                :disabled="currentStepIndex == 0"
                v-on:click="previousStep"
              >
                {{ previous }}
              </button>

              <button
                id="next"
                class="inline-flex items-center justify-center xs:w-20 xs:h-10 xs:text-sm sm md sm:w-44 sm:h-12 px-6 font-medium tracking-wide text-white transition duration-200 rounded shadow-md bg-teal-accent-400 enabled:hover:bg-teal-accent-600 focus:shadow-outline focus:outline-none ml-4 disabled:opacity-50"
                v-on:click="nextStep()"
              >
                {{ next }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useCheckedStore, useDataStore } from "../stores/checked";
import MessageError from "./MessageError.vue";
import CustomLoader from "./CustomLoader.vue";

import axios from "axios";
export default {
  name: "MultiStepForm",
  components: {
    MessageError,
    CustomLoader,
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
          checked: "",
        },
        {
          step: 4,
          checked: "",
        },
        {
          step: 5,
          checked: [],
        },
        {
          step: 6,
          checked: "",
        },
      ],
      errors: [],
      isError: null,
      currentStep: this.steps[0],
      currentStepIndex: this.steps.findIndex((step) => step.active),
      previous: "Previous",
      next: "Next",
      store: useCheckedStore(),
      dataStore: useDataStore(),
      maxChecked: 3,
      devices: [],
      loading: false,
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
  emits: ["devices"],
  computed: {
    checkboxMaxChecked() {
      return (
        this.formData[this.currentStepIndex].checked.length <= this.maxChecked
      );
    },
  },
  methods: {
    progressValue(index) {
      return (100 / this.steps.length) * index;
    },
    isStepCompleted(index) {
      return this.formData[index].checked.length > 0;
    },
    async submit() {
      let url = "/wphone/submit";
      let user = localStorage.getItem("username");
      let values = this.store.getAllValues;
      values.shift();

      let dailyUsage = values[0].checked[0];
      let mainUsage = values[1].checked[0];
      let storageSpace = values[2].checked[0];
      let displaySize = values[3].checked[0];
      let importantFeatures = values[4].checked[0];
      let budgetRange = values[5].checked[0];
      let data = {
        user: user ? user : "guest",
        dailyUsage: dailyUsage,
        mainUsage: mainUsage,
        storageSpace: storageSpace,
        displaySize: displaySize,
        importantFeatures: importantFeatures,
        budgetRange: budgetRange,
      };

      console.log("data", data);

      let config = {
        withCredentials: false,
        headers: {
          "Content-Type": "application/json",
        },
      };
      await axios.post(url, data, config).then((response) => {
        if (response.status === 200) {
          this.devices = response.data;

          if (this.devices.length === 0) {
            this.errors = ["No devices found. Please try again."];
            this.isError = true;
          } else {
            this.errors = [
              `Found ${this.devices.length} devices. Hope you like it.`,
            ];
            this.isError = false;
          }
          this.$emit("devices", this.devices);
          this.dataStore.setData(true);
          this.loading = false;
        } else {
          this.errors = ["Something went wrong. Please try again."];
          this.isError = true;
        }
      });
    },
    nextStep() {
      if (this.formData[this.currentStepIndex].checked.length === 0) {
        this.errors = ["Please select at least one option"];
        console.log(this.errors);
        this.isError = true;
      } else if (this.next === "Submit") {
        this.store.setCheckedByStep(
          this.formData[this.currentStepIndex].step,
          this.formData[this.currentStepIndex].checked
        );
        console.log("submit");
        if (this.compareData(this.formData, this.store.getAllValues)) {
          this.submit();
          this.loading = true;
        } else {
          this.errors = ["Something went wrong. Please try again."];
          this.isError = true;
        }
        this.previous = "Search again";
        document.getElementById("next").disabled = true;
        // disable checkbox and radio
        document.querySelectorAll("input").forEach((input) => {
          input.disabled = true;
        });
      } else {
        this.store.setCheckedByStep(
          this.formData[this.currentStepIndex].step,
          this.formData[this.currentStepIndex].checked
        );
        // this.currentStepIndex++;
        this.currentStepIndex++;
        this.currentStep = this.steps[this.currentStepIndex];
        console.log("currentStepIndex", this.currentStepIndex);
        console.log("currentStepIndex", this.currentStepIndex);
        console.log("currentStep", this.currentStep);
        this.closeMessageError();
      }
    },
    previousStep() {
      if (
        this.previous === "Search again" &&
        this.currentStepIndex === this.steps.length - 1
      ) {
        this.store.clearStore();
        this.devices = [];
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
            checked: "",
          },
          {
            step: 4,
            checked: "",
          },
          {
            step: 5,
            checked: [],
          },
          {
            step: 6,
            checked: "",
          },
        ];
        this.currentStepIndex = 0;
        this.currentStep = this.steps[this.currentStepIndex];
        // reset formData

        this.dataStore.setData(false);
      } else if (this.currentStepIndex > 0) {
        this.currentStepIndex--;
        this.currentStep = this.steps[this.currentStepIndex];
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

      if (this.currentStepIndex === this.steps.length - 1) {
        this.next = "Submit";
        this.previous = "Previous";
      } else if (this.currentStepIndex === 0) {
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
        if (
          this.formData[this.currentStepIndex].checked.length > this.maxChecked
        ) {
          this.errors = [`Please select at most ${this.maxChecked} options`];
          this.isError = true;
          console.log(this.errors);
          // remove first element of array
          this.formData[this.currentStepIndex].checked.shift();
          console.log(this.formData[this.currentStepIndex].checked);
        } else {
          this.errors = [];
        }
      }
    },
  },
  mounted() {
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
        checked: "",
      },
      {
        step: 4,
        checked: "",
      },
      {
        step: 5,
        checked: [],
      },
      {
        step: 6,
        checked: "",
      },
    ];
    this.currentStepIndex = 0;
    this.currentStep = this.steps[this.currentStepIndex];
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
</style>
