<template>
  <div class="column">
    <div class="card has-background-light">
      <div class="card-content">
        <div class="content has-text-centered">
          <div class="columns">
            <div class="column is-narrow">
              <b-icon
                :icon="icon"
                size="is-large"
                :type="'is-'+color"
              />
            </div>
            <div class="column">
              <div class="has-text-left">
                <span>お部屋の清潔度は</span>
                <p :class="'title is-4 has-text-'+color">{{ status }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    status: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    color: {
      type: String,
      required: true
    }
  }
}
</script>
