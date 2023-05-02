pkgname=htpgen
pkgver=0.0.1
pkgrel=1
pkgdesc="Simple lightweight .htpasswd line generator, no Apache required"
arch=("x86_64")
url="https://github.com/justalemon/htpgen"
license=("MIT")
depends=("python" "python-argparse" "python-bcrypt")

package() {
    install -m 775 -DT "$startdir/$pkgname.py" "$pkgdir/usr/bin/$pkgname"
}
