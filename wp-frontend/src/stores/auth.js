import { defineStore } from "pinia";
// import axios from "axios";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    // token: null,
    // isAuthenticated: false,
    access: null,
    refresh: null,
    username: null,
  }),
  getters: {
    getAccess: (state) => {
      return state.access;
    },
    getRefresh: (state) => {
      return state.refresh;
    },
    getUser: (state) => {
      return state.username;
    },
  },

  actions: {
    initializeStore() {
      let accessToken = localStorage.getItem("access");
      let refreshToken = localStorage.getItem("refresh");
      let userName = localStorage.getItem("username");

      if (accessToken) {
        this.access = accessToken;
        this.refresh = refreshToken;
        this.username = userName;
      } else {
        this.access = null;
        this.refresh = null;
        this.username = null;
      }
    },

    setAccess(access) {
      this.access = access;
      localStorage.setItem("access", access);
    },

    setRemoveAccess() {
      this.access = null;
      localStorage.removeItem("access");
      localStorage.removeItem("username");
      localStorage.removeItem("refresh");
      console.log("access removed");
    },

    setUser(username) {
      this.username = username;
      localStorage.setItem("username", username);
    },

    setRefresh(refresh) {
      this.refresh = refresh;
      localStorage.setItem("refresh", refresh);
    },
  },
});
