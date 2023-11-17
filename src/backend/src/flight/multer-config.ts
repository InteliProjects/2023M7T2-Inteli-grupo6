//multer-config.ts
import * as multerS3 from 'multer-s3';
import { S3Client } from '@aws-sdk/client-s3';
import * as path from 'path';
import { v4 as uuidv4 } from 'uuid';

require('dotenv').config();

const s3Config = new S3Client({
  region: 'us-east-1', //região selecionada na criação do bucket
  credentials: {
    accessKeyId: process.env.ACCESS_KEY_ID, //chave de acesso
    secretAccessKey: process.env.SECRET_ACCESS_KEY, //chave de acesso secreta
    sessionToken: process.env.SESSION_TOKEN,
  },
});

const multerConfig = {
  storage: multerS3({
    s3: s3Config,
    bucket: process.env.BUCKET_FILE,
    contentType: multerS3.AUTO_CONTENT_TYPE,
    key: (request, file, callback) => {
      const fileName =
        path.parse(file.originalname).name.replace(/\s/g, '') + '-' + uuidv4();

      const extension = path.parse(file.originalname).ext;
      callback(null, `${fileName}${extension}`);
    },
  }),
  limits: {
    fileSize: 100 * 1024 * 1024, // Permitir arquivos até 100MB
  },
};

export default multerConfig;
