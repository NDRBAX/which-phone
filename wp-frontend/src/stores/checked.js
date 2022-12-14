import { defineStore } from "pinia";
import { useAuthStore } from "./auth";
import axios from "axios";

export const useCheckedStore = defineStore({
  id: "checked",
  state: () => ({
    values: [
      {
        step: null,
        checked: [],
      },
    ],
  }),

  getters: {
    getValuesByStep: (state) => (step) => {
      return state.values[step];
    },
    getAllValues: (state) => {
      return state.values;
    },
  },
  actions: {
    setCheckedByStep(step, checked) {
      // check if step exists
      if (this.values[step]) {
        // remove the step
        this.values.splice(step, 1);
        this.values.splice(step, 0, {
          step: step,
          checked: [checked],
        });
      } else {
        this.values[step] = {
          step: step,
          checked: [checked],
        };
      }
      console.log(this.getAllValues);
    },

    clearStore() {
      this.values = [
        {
          step: null,
          checked: [],
        },
      ];
      console.log("cleared");
      console.log(this.getAllValues);
    },

    async submit() {
      let url = "/wphone/submit";
      let user = useAuthStore().getUser;
      let values = this.getAllValues;
      values.shift();
      let data = {};

      if (user === null) {
        data = {
          user: "guest",
          values: values,
        };
        console.log("values", values);
      } else {
        data = {
          user: user,
          values: values,
        };
      }

      let jsonData = JSON.stringify(data);
      console.log("jsonData", jsonData);

      console.log(this.getAllValues);
      let config = {
        withCredentials: false,
        headers: {
          "Content-Type": "application/json",
        },
      };
      await axios.post(url, jsonData, config);
    },
  },
});
