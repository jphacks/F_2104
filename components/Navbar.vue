<template>
  <b-navbar>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <h1 class="is-size-2">
          掃除しなくちゃ
        </h1>
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item href="#">
        データを見る
      </b-navbar-item>
    </template>
    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-primary">
            <strong>アカウントの作成</strong>
          </a>
          <a class="button is-light">
            ログイン
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>
