import { defineStore } from "pinia";
// import axios from "axios";

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    access: null,
    refresh: null,
    username: null,
    avatar: null,
    email: null,
    historyCount: null,
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
    getAvatar: (state) => {
      return state.avatar;
    },
    getEmail: (state) => {
      return state.email;
    },
    getHistoryCount: (state) => {
      return parseInt(state.historyCount);
    },
  },

  actions: {
    initializeStore() {
      let accessToken = localStorage.getItem("access");
      let refreshToken = localStorage.getItem("refresh");
      let userName = localStorage.getItem("username");
      let avatar = localStorage.getItem("avatar");
      let email = localStorage.getItem("email");
      let historyCount = localStorage.getItem("historyCount");

      if (accessToken) {
        this.access = accessToken;
        this.refresh = refreshToken;
        this.username = userName;
        this.avatar = avatar;
        this.email = email;
        this.historyCount = historyCount;
      } else {
        this.access = null;
        this.refresh = null;
        this.username = null;
        this.avatar = null;
        this.email = null;
        this.historyCount = null;
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
      localStorage.removeItem("avatar");
      localStorage.removeItem("email");
      localStorage.removeItem("historyCount");
      console.log("access removed");
    },

    setUser(username) {
      this.username = username;
      localStorage.setItem("username", username);
    },

    setAvatar(avatar) {
      this.avatar = avatar;
      localStorage.setItem("avatar", avatar);
    },

    setEmail(email) {
      this.email = email;
      localStorage.setItem("email", email);
    },

    setHistoryCount(count) {
      this.historyCount = count;
      localStorage.setItem("historyCount", count);
    },

    setRefresh(refresh) {
      this.refresh = refresh;
      localStorage.setItem("refresh", refresh);
    },
  },
});
