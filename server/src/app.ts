import { Server } from 'http'
import express, { Application, Request, Response, NextFunction } from 'express'
import passport from 'passport'
import * as defaultConfig from './defaultConfig'
import loadPassport from './loadpassport'
import mainRouter from './mainRouter';



class App {
    private config: any;
    private app: Application;
    private server?: Server;

    constructor(config?: any) {
        this.app = express();
        this.config = {
            ...defaultConfig,
            ...config
        }

        this.configure();
    }

    listen = (port: number = this.config.port, host: string = this.config.host)=> {
        this.server = this.app.listen(port, host, () => {
            console.log(`>>> App is Ready on port ${port}`)
        })
        return this.server
    }

    private configure (app: Application = this.app, config: any = this.config) {
        loadPassport(passport)

        app.use(passport.initialize());
        app.use(passport.session());
        app.use(config.mountPoint, mainRouter)

        app.use((err: any, req: Request, res: Response, next: NextFunction) => {
            next()
        })
    }
}
export default App