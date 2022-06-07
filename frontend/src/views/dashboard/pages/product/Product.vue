<template>
  <v-container
    id="product"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Editar Produto
            </div>

            <!-- <div class="text-subtitle-1 font-weight-light">
              Complete your profile
            </div> -->
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Preço"
                    value="12.00"
                  />
                </v-col>

                <v-col cols="12">
                  <v-text-field
                    class="purple-input"
                    label="Título"
                    value="Condicionador"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-textarea
                    class="purple-input"
                    label="Descrição"
                    value="Fall myself run house improve oil citizen theory."
                  />
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
                  >
                    Salvar
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>

      <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
          avatar=""
        >
          <v-card-text class="text-center">
            <!-- <h6 class="display-1 mb-1 grey--text">
              CEO / CO-FOUNDER
            </h6> -->

            <h4 class="text-h3 font-weight-light mb-3 black--text">
              Condicionador
            </h4>

            <p class="font-weight-light grey--text">
              Fall myself run house improve oil citizen theory.
            </p>

            <img
              src="https://res.cloudinary.com/mtree/image/upload/w_750,q_auto:eco,f_auto,dpr_auto/pantene-br/Lf3XZD165XAln9vl7VxmS/8aeb39af03c443567f26297eb6258f8a/HIDROCAUTERIZACAO_Mobile__320x540_07506309840581_C1N1.png"
              width="150"
              alt="condicionador"
            >

            <!-- <v-btn
              color="success"
              rounded
              class="mr-0"
            >
              Follow
            </v-btn> -->
          </v-card-text>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    //
  }
</script>
