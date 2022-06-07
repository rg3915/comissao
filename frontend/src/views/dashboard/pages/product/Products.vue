<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Produtos"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Importado
            </th>
            <th class="primary--text">
              Fora de Linha
            </th>
            <th class="primary--text">
              Título
            </th>
            <th class="primary--text">
              Descrição
            </th>
            <th class="primary--text">
              Preço
            </th>
            <th class="primary--text">
              Foto
            </th>
            <th class="text-right primary--text">
              Editar
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td v-if="item.imported">
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check
              </v-icon>
            </td>
            <td v-else>
              <v-icon
                class="mx-1"
                style="color: red"
              >
                mdi-close
              </v-icon>
            </td>
            <td v-if="item.outline">
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check
              </v-icon>
            </td>
            <td v-else>
              <v-icon
                class="mx-1"
                style="color: red"
              >
                mdi-close
              </v-icon>
            </td>
            <td>
              <a href="#/pages/product/product">{{ item.title }}</a>
            </td>
            <td>{{ item.description }}</td>
            <td>R$ <span class="float-right">{{ item.price }}</span></td>
            <td />
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            title: 'Shampoo',
            description: 'Others skin perhaps.',
            price: 22,
            imported: true,
            outline: true,
          },
          {
            title: 'Condicionador',
            description: 'Fall myself run house improve oil citizen theory.',
            price: 25.09,
            imported: true,
            outline: true,
          },
          {
            title: 'Hidratante',
            description: 'Assume not road.',
            price: 43.09,
            imported: true,
            outline: false,
          },
          {
            title: 'Máscara de tratamento',
            description: 'Even soon spring.',
            price: 1200.99,
            imported: true,
            outline: false,
          },
          {
            title: 'Finalizador',
            description: 'Already sign employee international quality human.',
            price: 12,
            imported: false,
            outline: true,
          },
          {
            title: 'Liso para escova progressiva',
            description: 'Point who financial town head claim.',
            price: 23.01,
            imported: false,
            outline: true,
          },
          {
            title: 'Tesoura de ponta fina',
            description: 'See reflect put big least whom.',
            price: 32.99,
            imported: false,
            outline: false,
          },
          {
            title: 'Pente',
            description: 'Eye student each conference term while must.',
            price: 23.12,
            imported: true,
            outline: true,
          },
          {
            title: 'Escova',
            description: 'Order we receive hour bar.',
            price: 28.99,
            imported: true,
            outline: true,
          },
          {
            title: 'Primer',
            description: 'Drop left as eat.',
            price: 32.01,
            imported: true,
            outline: true,
          },
          {
            title: 'Base',
            description: 'Marriage group true stop site book.',
            price: 10.08,
            imported: false,
            outline: false,
          },
          {
            title: 'Pó',
            description: 'Ability during possible statement hard stand.',
            price: 7.32,
            imported: true,
            outline: true,
          },
          {
            title: 'Demaquilante',
            description: 'Together school this.',
            price: 8.99,
            imported: true,
            outline: true,
          },
        ],
      }
    },
  }
</script>
