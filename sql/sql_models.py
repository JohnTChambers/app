from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqla

Base = declarative_base()

class BasicGenomeData(Base):
    __tablename__ = 'basic_genome_data'

    species = sqla.Column(sqla.String(64), primary_key=True)
    latin_name = sqla.Column(sqla.String(64))
    gene_number = sqla.Column(sqla.Integer)
    gene_number = sqla.Column(sqla.Integer)
    genome_length = sqla.Column(sqla.Integer)
    chr_number = sqla.Column(sqla.Integer)
    splice_rate = sqla.Column(sqla.String(64))

    def __repr__(self):
        return f"'Species': {self.species}   " \
               f"'Latin name': {self.latin_name}   " \
               f"'gene_number': {self.gene_number}   " \
               f"'genome_length': {self.genome_length}   " \
               f"'chr_number': {self.chr_number}   " \
               f"'splice_Rate': {self.splice_rate}"